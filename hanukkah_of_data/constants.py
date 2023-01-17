from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
PACKAGE_PATH = ROOT_PATH / "hanukkah_of_data"
TWENTY_TWENTY_TWO_PATH = PACKAGE_PATH / "twenty_twenty_two"
TWENTY_TWENTY_TWO_DATA_PATH = TWENTY_TWENTY_TWO_PATH / "data"

YEARS_MAP = {
    "5777": {
        "local_path": TWENTY_TWENTY_TWO_PATH,
        "data_path": TWENTY_TWENTY_TWO_DATA_PATH,
        "url": "https://hanukkah.bluebird.sh/5783/noahs-csv.zip",
        "pwd": "5777",
    }
}

DTYPES_MAP = {
    "customers": {
        "customerid": int,
        "name": "string",
        "address": "string",
        "citystatezip": "string",
        "birthdate": "string",
        "phone": "string",
    },
    "orders": {
        "orderid": int,
        "customerid": int,
        "ordered": "string",
        "shipped": "string",
        "items": float,
        "total": float,
    },
    "orders_items": {"orderid": int, "sku": "string", "qty": int, "unit_price": float},
    "products": {"sku": "string", "desc": "string", "wholesale_cost": float},
}

DATE_COLUMN_MAP = {
    "customers": ["birthdate"],
    "orders": ["ordered", "shipped"],
    "orders_items": None,
    "products": None,
}
