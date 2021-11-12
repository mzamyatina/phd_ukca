import iris

EXPERIMENTS = {
    "CTRL": "xojng",  # MeONO2 initialised with zero
    "CHEM": "xojnh",  # MeONO2 initialised with zero
    "MARI": "xojni",  # MeONO2 initialised with zero
    "FIRE": "xojnw",  # MeONO2 initialised with zero; unexplained jump in burdens; same as xojnv but 193 months and faulty data removed
    "FULL": "xojnl",  # MeONO2 initialised with zero
    #     'ORIG'    :'xolnb', # original CheST
    #     'UPDT'    :'xolna', # updated CheST
}

# Experiments present in thesis only
# "BASE OLD": "xojnd", # called SSAN; MeONO2 initialised with a non-zero steady state value from Banerjee2014 “Base”
# "FIRE OLD": "xojnc", # called FIRE; MeONO2 initialised with a non-zero steady state value from Banerjee2014 “Base”; iPrONO2 is chemically active, but no iPrONO2 ouput

# Experiments history
# CHEM xojne had a strange O3 burden
# MARI xojnb MeONO2 initialised with a non-zero steady state value from Banerjee2014 “Base” and no n/iPrONO2 oceanic emissions
# FIRE xojnv MeONO2 initialised with zero; unexplained jump in burdens; 139 months
# FULL xojnk had a wrong setup

STASH = {
    "main": {
        "temp": "air_temperature",
        "air_mass": "m01s34i363",
        "trop_mask": "m01s34i362",
        "ch4": "mass_fraction_of_methane_in_air",
        "c2h6": "mass_fraction_of_ethane_in_air",
        "c3h8": "mass_fraction_of_propane_in_air",  # m01s34i018
        "no": "mass_fraction_of_nitrogen_monoxide_in_air",
        "no2": "m01s34i152",
        "meono2": "mass_fraction_of_methyl_nitrate_in_air",
        "etono2": "m01s34i096",  # was output using mass_fraction_of_methyl_ethyl_ketone_in_air stash code
        "nprono2": "m01s34i097",  # was output using mass_fraction_of_toluene_in_air stash code
        "iprono2": "m01s34i098",
        "hono": "mass_fraction_of_nitrous_acid_in_air",
        "ho2no2": "mass_fraction_of_peroxynitric_acid_in_air",
        "hno3": "mass_fraction_of_nitric_acid_in_air",
        "n2o5": "mass_fraction_of_dinitrogen_pentoxide_in_air",
        "pan": "mass_fraction_of_peroxyacetyl_nitrate_in_air",
        "ppan": "mass_fraction_of_peroxypropionyl_nitrate_in_air",
        "o3": "mass_fraction_of_ozone_in_air",
        "oh": "mass_fraction_of_hydroxyl_radical_in_air",
    },
    "extra": {
        "trop_alt": "tropopause_altitude",
        "co": "mass_fraction_of_carbon_monoxide_in_air",
        "ho2": "mass_fraction_of_hydroperoxyl_radical_in_air",
        "meoo": "mass_fraction_of_methyl_peroxy_radical_in_air",  # m01s34i083
        "etoo": "mass_fraction_of_ethyl_peroxy_radical_in_air",  # m01s34i084
        "nproo": "mass_fraction_of_n-propylperoxy_radical_in_air",  # m01s34i086
        "iproo": "mass_fraction_of_isopropylperoxy_radical_in_air",  # m01s34i087
        "hcho": "mass_fraction_of_formaldehyde_in_air",
        "mecho": "mass_fraction_of_acetaldehyde_in_air",
        "etcho": "mass_fraction_of_propanal_in_air",
        "me2co": "mass_fraction_of_acetone_in_air",
    },
}

GASES = {
    #     "main": {
    "ch4": {"tex": "$CH_4$", "molar_mass": 16.0425, "ppn": "ppbv", "rh": True},
    "c2h6": {
        "tex": "$C_2H_6$",
        "molar_mass": 30.0690,
        "ppn": "pptv",
        "rh": True,
    },  # "pptvC"
    "c3h8": {"tex": "$C_3H_8$", "molar_mass": 44.0956, "ppn": "pptv", "rh": True},
    "no": {"tex": "NO", "molar_mass": 30.006, "ppn": "ppbv", "nox": True, "noy": True},
    "no2": {
        "tex": "$NO_2$",
        "molar_mass": 46.006,
        "ppn": "ppbv",
        "nox": True,
        "noy": True,
    },
    "nox": {
        "tex": "$NO_x$",
        "ppn": "ppbv",
    },
    "meono2": {
        "tex": "$MeONO_2$",
        "molar_mass": 77.0394,
        "ppn": "pptv",
        "nox": False,
        "noy": True,
    },
    "etono2": {
        "tex": "$EtONO_2$",
        "molar_mass": 91.066,
        "ppn": "pptv",
        "nox": False,
        "noy": True,
    },
    "nprono2": {
        "tex": "$nPrONO_2$",
        "molar_mass": 105.0926,
        "ppn": "pptv",
        "nox": False,
        "noy": True,
    },
    "iprono2": {
        "tex": "$iPrONO_2$",
        "molar_mass": 105.0926,
        "ppn": "pptv",
        "nox": False,
        "noy": True,
    },
    "hono": {
        "tex": "HONO",
        "molar_mass": 47.013,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "ho2no2": {
        "tex": "$HO_2NO_2$",
        "molar_mass": 79.01224,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "hno3": {
        "tex": "$HNO_3$",
        "molar_mass": 63.012,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "n2o5": {
        "tex": "$N_2O_5$",
        "molar_mass": 108.01,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "pan": {
        "tex": "PAN",
        "molar_mass": 121.0489,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "ppan": {
        "tex": "PPN",
        "molar_mass": 135.0755,
        "ppn": "ppbv",
        "nox": False,
        "noy": True,
    },
    "noy": {
        "tex": "$NO_y$",
        "ppn": "ppbv",
    },
    "o3": {
        "tex": "$O_3$",
        "molar_mass": 47.997,
        "ppn": "ppbv",
    },
    "oh": {
        "tex": "OH",
        "molar_mass": 17.007,
        "ppn": "pptv",
    },
    "air": {"molar_mass": 28.9644},
    #     },
    #     "extra": {
    "co": {
        "tex": "CO",
        "molar_mass": 28.010,
    },
    "ho2": {
        "tex": "$HO_2$",
        "molar_mass": 33.006,
    },
    "meoo": {
        "tex": "MeOO",
        "molar_mass": 47.0333,
    },
    "etoo": {
        "tex": "EtOO",
        "molar_mass": 61.0599,
    },
    "nproo": {
        "tex": "nPrOO",
        "molar_mass": 75.0865,
    },
    "iproo": {
        "tex": "iPrOO",
        "molar_mass": 75.0865,
    },
    "hcho": {
        "tex": "HCHO",
        "molar_mass": 30.0260,
    },
    "mecho": {
        "tex": "MeCHO",
        "molar_mass": 44.0526,
    },
    "etcho": {
        "tex": "EtCHO",
        "molar_mass": 58.0791,
    },
    "me2co": {
        "tex": "Me2CO",
        "molar_mass": 58.0791,
    },
    #     },
}

LAYERS = {
    "0-2km": {
        "iris_constr": iris.Constraint(level_height=lambda cell: 0 <= cell <= 2000),
        "tex": "Boundary layer (0-2 km)",
    },
    "5-10km": {
        "iris_constr": iris.Constraint(level_height=lambda cell: 5000 <= cell <= 10000),
        "tex": "Free troposphere (5-10 km)",
    },
    "0-17km": {
        "iris_constr": iris.Constraint(level_height=lambda cell: 0 <= cell <= 17000),
        "tex": "Troposphere (0-17 km)",
    },
    "0-85km": {
        "iris_constr": iris.Constraint(level_height=lambda cell: 0 <= cell <= 90000),
        "tex": "Troposphere and stratosphere (0-85 km)",
    },
}

SEASONS = {
    "djf": {"iris_constr": iris.Constraint(season="djf")},
    "mam": {"iris_constr": iris.Constraint(season="mam")},
    "jja": {"iris_constr": iris.Constraint(season="jja")},
    "son": {"iris_constr": iris.Constraint(season="son")},
}
