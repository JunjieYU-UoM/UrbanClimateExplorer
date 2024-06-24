cesm1 = {
    "model": "cesm1",
    "urban_type": "md",
    "city_loc": {
        "lat": 40.0150,
        "lon": -105.2705
    },
    "l_component": "lnd",
    "a_component": "atm",
    "experiment": "RCP85",
    "frequency": "daily",
    "cam_ls": [
        "TREFHT",
        "TREFHTMX",
        "FLNS",
        "FSNS",
        "PRECSC",
        "PRECSL",
        "PRECT",
        "QBOT",
        "UBOT",
        "VBOT"
    ],
    "clm_ls": [
        "TREFMXAV_U"
    ],
    "forcing_variant": "cmip6",
    "time_start": "2081-01-02",
    "time_end": "2100-12-31",
    "member_id": [
        2
    ],
    "estimator_list": [
        "lgbm",
        "xgboost",
        "rf",
        "extra_tree"
    ],
    "time_budget": 15,
    "features": [
        "FLNS",
        "FSNS",
        "PRECT",
        "PRSN",
        "QBOT",
        "TREFHT",
        "UBOT",
        "VBOT"
    ],
    "label": [
        "TREFMXAV_U"
    ]
}

cesm2 = {
    "model": "cesm2",
    "urban_type": "md",
    "city_loc": {
        "lat": 40.0150,
        "lon": -105.2705
    },
    "l_component": "lnd",
    "a_component": "atm",
    "experiment": "ssp370",
    "frequency": "daily",
    "cam_ls": [
        "TREFHT",
        "TREFHTMX",
        "FLNS",
        "FSNS",
        "PRECSC",
        "PRECSL",
        "PRECC",
        "PRECL"
    ],
    "clm_ls": [
        "TREFMXAV"
    ],
    "forcing_variant": "cmip6",
    "time_start": "2081-01-02",
    "time_end": "2100-12-31",
    "member_id": [
        "r1i1231p1f1"
    ],
    "estimator_list": [
        "lgbm",
        "xgboost",
        "rf",
        "extra_tree"
    ],
    "time_budget": 15,
    "features": [
        "FLNS",
        "FSNS",
        "PRECT",
        "PRSN",
        "TREFHT"
    ],
    "label": [
        "TREFMXAV"
    ]
}

cesm2_climate_future = {
    "model": "cesm2",
    "urban_type": "md",
    "city_loc": {
        "lat": 40.0150,
        "lon": -105.2705
    },
    "l_component": "lnd",
    "a_component": "atm",
    "experiment": "ssp370",
    "frequency": "daily",
    "cam_ls": [
        "TREFHT",
        "TREFHTMX",
        "TREFHTMN",
        "FLNS",
        "FSNS",
        "PRECSC",
        "PRECSL",
        "PRECC",
        "PRECL"
    ],
    "clm_ls": [
        "TREFMXAV"
    ],
    "forcing_variant": "cmip6",
    "time_start": "2066-01-02",
    "time_end": "2085-12-31",
    "member_id": [
        "r1i1231p1f1"
    ],
    "estimator_list": [
        "lgbm",
        "xgboost",
        "rf",
        "extra_tree"
    ],
    "time_budget": 30,
    "features": [
        "FLNS",
        "FSNS",
        "PRECT",
        "PRSN",
        "TREFHT",
        "TREFHTMX",
        "TREFHTMN"
    ],
    "label": [
        "TREFMXAV"
    ]
}

cesm2_climate_present = {
    "model": "cesm2",
    "urban_type": "md",
    "city_loc": {
        "lat": 40.0150,
        "lon": -105.2705
    },
    "l_component": "lnd",
    "a_component": "atm",
    "experiment": "ssp370",
    "frequency": "daily",
    "cam_ls": [
        "TREFHT",
        "TREFHTMX",
        "TREFHTMN",
        "FLNS",
        "FSNS",
        "PRECSC",
        "PRECSL",
        "PRECC",
        "PRECL"
    ],
    "clm_ls": [
        "TREFMXAV"
    ],
    "forcing_variant": "cmip6",
    "time_start": "2016-01-02",
    "time_end": "2035-12-31",
    "member_id": [
        "r1i1231p1f1"
    ],
    "estimator_list": [
        "lgbm",
        "xgboost",
        "rf",
        "extra_tree"
    ],
    "time_budget": 30,
    "features": [
        "FLNS",
        "FSNS",
        "PRECT",
        "PRSN",
        "TREFHT",    
        "TREFHTMX",
        "TREFHTMN"
    ],
    "label": [
        "TREFMXAV"
    ]
}
    

cesm2_to_cmip6 = {
    "model": "cesm2",
    "urban_type": "md",
    "city_loc": {
        "lat": 40.0150,
        "lon": -105.2705
    },
    "l_component": "lnd",
    "a_component": "atm",
    "experiment": "ssp370",
    "frequency": "daily",
    "cam_ls": [
        "PRECC", 
        "PRECL", 
        "PRECSC", 
        "PRECSL",
        "PSL",
        "TREFHT",
        "TREFHTMN",
        "TREFHTMX"
    ],
    "clm_ls": [
        "TREFMXAV"
    ],
    "forcing_variant": "cmip6",
    "time_start": "2081-01-02",
    "time_end": "2100-12-31",
    "member_id": [
        "r1i1231p1f1"
    ],
    "estimator_list": [
        "lgbm",
        "xgboost",
        "rf",
        "extra_tree"
    ],
    "time_budget": 15,
    "features":[
        "pr",
        "prsn",
        "psl",
        "tas",
        "tasmax",
        "tasmin"
    ],
    "label": [
        "TREFMXAV"
    ],
    "CMIP6_url": "https://cmip6-pds.s3.amazonaws.com/pangeo-cmip6.json",
    "activity_id": "ScenarioMIP",
    "experiment_id": "ssp370",
    "institution_id": "NOAA-GFDL",
    "table_id": "day"
}