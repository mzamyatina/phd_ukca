from util_commons import GASES

import iris

import numpy as np

from scipy import stats

from aeolus.coord import add_cyclic_point_to_cube


def mmr_to_vmr(molar_mass, air_mass=28.97):
    """Convert mass mixing ratio to volume mixing ratio."""
    return air_mass / molar_mass


# # Add mass mixing ratio to volume mixing ratio conversion coefficient to GASES
# for k, v in GASES.items():
#     try:
#         GASES[k]["mmr_to_vmr"] = mmr_to_vmr(GASES[k]["molar_mass"])
#     except KeyError:
#         pass


def mmr_to_vmr_in_ppn(arr_mmr, molar_mass, ppn):
    M_air = 28.97  # molar mass of dry air [g mol-1]
    if ppn == "ppbv":
        power_of_ten = 1e9
    if ppn == "pptv" or ppn == "pptvC":
        power_of_ten = 1e12
    arr_vmr = arr_mmr * (M_air / molar_mass) * power_of_ten
    return arr_vmr


def calc_mean_diff_pval(cube_ctrl, cube_sens, pval_thresh=0.05):
    """Find if the mean difference in the chemical species abundance between the control and sensitivity experiment is statisticaly significant.

    1. Check if the data are normally distributed using the Shapiro–Wilk test.
    2. If the data are normally distributed, use a paired sample t-test, and if not, use the Wilcoxon signed-rank test.
    cube_ctrl and cube_sens must contain 9-year-average seasonal means in a chosen atmospheric layer for each latitude-longitude.

    Parameters
    ----------
    cube_ctrl: iris.cube.Cube
        Cube with the data from the control experiment.
    cube_sens: iris.cube.Cube
        Cube with the data from the sensitivity experiment.
    pval_thresh: float, optional
        p-value threshold.

    Returns
    -------
    iris.cube.Cube
        Cube of p-values.
    """
    result_cube_dummy = next(cube_ctrl.slices_over("time"))
    nlats, nlons = result_cube_dummy.shape
    pval_arr = np.empty([nlats, nlons])
    for j in range(nlats):
        for i in range(nlons):
            shapiro_pval = stats.shapiro(
                cube_ctrl.data[:, j, i] - cube_sens.data[:, j, i]
            )[1]
            if shapiro_pval > pval_thresh:
                pval_arr[j, i] = stats.ttest_rel(
                    cube_ctrl.data[:, j, i], cube_sens.data[:, j, i]
                )[1]
            else:
                pval_arr[j, i] = stats.wilcoxon(
                    cube_ctrl.data[:, j, i], cube_sens.data[:, j, i]
                )[1]
    cube_out = result_cube_dummy.copy(data=pval_arr)
    cube_out.rename("p-value")
    cube_out.units = 1
    return cube_out


def fdr_threshold(pval_arr, alpha=0.05 * 2):
    """Compute the false discovery rate threshod after Wilks (2016).
    Credit to https://fabienmaussion.info/2017/01/30/trendy-triangles-fdr/"""
    p = np.sort(np.asarray(pval_arr).flatten())
    n = len(p)
    return np.max(np.where(p <= np.arange(1, n + 1) / n * alpha, p, 0))


def stipple_out(cube_pval, fdr_on=True):
    """Stipple areas where the mean difference in the chemical species abundance between the control and sensitivity experiment is not statisticaly significant.

    Parameters
    ----------
    cube_pval: iris.cube.Cube
        Cube of p-values.
    fdr_on: bool
        Use the false discovery rate threshold instead of the original p-value.

    Returns
    -------
    tuple
        Coordinates to stipple out.
    """
    coord_points = [c.points for c in cube_pval.dim_coords]
    mesh_grids = np.meshgrid(*coord_points[::-1])
    if fdr_on:
        thresh = fdr_threshold(cube_pval.data)
    else:
        thresh = 0.05
    pval_above_thresh = cube_pval.data > thresh
    coord_points_above_thresh = [arr[pval_above_thresh] for arr in mesh_grids]
    return coord_points_above_thresh


def calc_seasonal_mean_in_layer(cube, season, layer):
    """Calculate seasonal mean in a specified layer and add a cyclic longitude."""
    ssn = iris.Constraint(season=season)
    cb = cube.extract(ssn & layer).collapsed(
        ["season", "level_height"], iris.analysis.MEAN
    )
    cyclic_cb = add_cyclic_point_to_cube(cb)
    return cyclic_cb
