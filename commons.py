import iris

EXPERIMENTS = {
    "BASE OLD": "xojnd",
    "BASE": "xojng",
    "CHEM": "xojnh",
    "MARI": "xojni",
    "FIRE": "xojnv", # c vs BASE OLD or v/w vs BASE
    "FULL": "xojnl",
}

GASES = {
    "no": {"tex": "NO", "molar_mass": 30.006, "nox": True, "noy": True},
    "no2": {"tex": "$NO_2$", "molar_mass": 46.006, "nox": True, "noy": True},
    "hono": {"tex": "HONO", "molar_mass": 47.013, "nox": False, "noy": True},
    "ho2no2": {"tex": "$HO_2NO_2$", "molar_mass": 79.01224, "nox": False, "noy": True},
    "hno3": {"tex": "$HNO_3$", "molar_mass": 63.012, "nox": False, "noy": True},
    "n2o5": {"tex": "N_2O_5", "molar_mass": 108.01, "nox": False, "noy": True},
    "pan": {"tex": "PAN", "molar_mass": 121.0489, "nox": False, "noy": True},
    "ppan": {"tex": "PPN", "molar_mass": 135.0755, "nox": False, "noy": True},
    "meono2": {"tex": "$MeONO_2$", "molar_mass": 77.0394, "nox": False, "noy": True},
    "etono2": {"tex": "$EtONO_2$", "molar_mass": 91.066, "nox": False, "noy": True},
    "nprono2": {"tex": "$nPrONO_2$", "molar_mass": 105.0926, "nox": False, "noy": True},
    "iprono2": {"tex": "$iPrONO_2$", "molar_mass": 105.0926, "nox": False, "noy": True},
    "nox": {"tex": "$NO_x$", "nox": False, "noy": False},
    "noy": {"tex": "$NO_y$", "nox": False, "noy": False},
    "ch4": {"tex": "$CH_4$", "molar_mass": 16.0425, "nox": False, "noy": False},
    "o3": {"tex": "$O_3$", "molar_mass": 47.997, "nox": False, "noy": False},
}

LAYERS = {
    "boundary": iris.Constraint(level_height=lambda cell: 0 <= cell <= 2000),
    "free troposphere": iris.Constraint(level_height=lambda cell: 2000 <= cell <= 6000),
}

SEASONS = ["djf", "mam", "jja", "son"]
