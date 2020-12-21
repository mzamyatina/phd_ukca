from commons import GASES

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


def calc_seasonal_mean_in_layer(cube, season, layer):
    """Calculate seasonal mean in a specified layer and add a cyclic longitude."""
    ssn = iris.Constraint(season=season)
    cb = cube.extract(ssn & layer).collapsed(
        ["season", "level_height"], iris.analysis.MEAN
    )
    cyclic_cb = add_cyclic_point_to_cube(cb)
    return cyclic_cb
