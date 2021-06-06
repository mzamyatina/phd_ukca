from util_commons import GASES

import iris

from aeolus.coord import add_cyclic_point_to_cube


def mmr_to_vmr(molar_mass, air_mass=28.97):
    """Convert mass mixing ratio to volume mixing ratio."""
    return air_mass / molar_mass


# Add mass mixing ratio to volume mixing ratio conversion coefficient to GASES
for k, v in GASES.items():
    try:
        GASES[k]["mmr_to_vmr"] = mmr_to_vmr(GASES[k]["molar_mass"])
    except KeyError:
        pass
    
def mmr_to_vmr_in_ppn(arr_mmr, molar_mass, ppn):
    M_air = 28.97  # molar mass of dry air [g mol-1]
    if ppn == "ppbv":
        power_of_ten = 1e9
    if ppn == "pptv" or ppn == "pptvC":
        power_of_ten = 1e12
    arr_vmr = arr_mmr * (M_air / molar_mass) * power_of_ten
    return arr_vmr


def calc_seasonal_mean_in_layer(cube, season, layer):
    """Calculate seasonal mean in a specified layer and add a cyclic longitude."""
    ssn = iris.Constraint(season=season)
    cb = cube.extract(ssn & layer).collapsed(
        ["season", "level_height"], iris.analysis.MEAN
    )
    cyclic_cb = add_cyclic_point_to_cube(cb)
    return cyclic_cb


def fdr_threshold(pvalues, alpha=0.05 * 2):
    """Compute the FDR threshod after Wilks (2016).
    Credit to https://fabienmaussion.info/2017/01/30/trendy-triangles-fdr/"""
    p = np.sort(np.asarray(pvalues).flatten())
    n = len(p)
    return np.max(np.where(p <= np.arange(1, n + 1) / n * alpha, p, 0))


def stipple_bl(cube, pval_arr, fdr, central_long=0):
    """Stipple areas where p-values are statistically significant.
    Inspired by https://groups.google.com/forum/#!topic/scitools-iris/Xm2IhQ6YKQA"""
    xOrg = cube.coord("longitude").points
    yOrg = cube.coord("latitude").points
    nlon = len(xOrg)
    nlat = len(yOrg)
    xData = np.reshape(np.tile(xOrg, nlat), pval_arr.shape)
    yData = np.reshape(np.repeat(yOrg, nlon), pval_arr.shape)
    if fdr:
        thresh = fdr_threshold(pval_arr)  # false discovery rate threshold
    else:
        thresh = 0.05
    sigPoints = pval_arr < thresh
    xPoints = xData[sigPoints] - central_long
    yPoints = yData[sigPoints]
    return (xPoints, yPoints)
