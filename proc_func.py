from commons import GASES


def mmr_to_vmr(molar_mass, air_mass=28.97):
    """Convert mass mixing ratio to volume mixing ratio."""
    return air_mass / molar_mass


# Add mass mixing ratio to volume mixing ratio conversion coefficient to GASES
for k, v in GASES.items():
    try:
        GASES[k]["mmr_to_vmr"] = mmr_to_vmr(GASES[k]["molar_mass"])
    except KeyError:
        pass
