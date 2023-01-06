import urllib.request
from zipfile import ZipFile

import pandas as pd

from hanukkah_of_data.constants import (
    DATE_COLUMN_MAP,
    DTYPES_MAP,
    TWENTY_TWENTY_TWO_DATA_PATH,
    TWENTY_TWENTY_TWO_PWD,
    TWENTY_TWENTY_TWO_URL,
)


def download_data() -> None:
    if not TWENTY_TWENTY_TWO_DATA_PATH.joinpath("data.zip").exists():
        print(
            f"Downloading data from {TWENTY_TWENTY_TWO_URL} to {TWENTY_TWENTY_TWO_DATA_PATH}/data.zip"
        )
        urllib.request.urlretrieve(
            TWENTY_TWENTY_TWO_URL, TWENTY_TWENTY_TWO_DATA_PATH.joinpath("data.zip")
        )
    else:
        print(f"Data already downloaded to {TWENTY_TWENTY_TWO_DATA_PATH}/data.zip")


def extract_data() -> None:
    if TWENTY_TWENTY_TWO_DATA_PATH.joinpath("data.zip").exists():
        if not list(TWENTY_TWENTY_TWO_DATA_PATH.glob("*.csv")):
            with ZipFile(TWENTY_TWENTY_TWO_DATA_PATH.joinpath("data.zip")) as f:
                f.extractall(
                    path=TWENTY_TWENTY_TWO_DATA_PATH,
                    pwd=str.encode(TWENTY_TWENTY_TWO_PWD),
                )
        else:
            print("Data has already been extracted.")
    else:
        print(f"File 'data.zip' does not exist in {TWENTY_TWENTY_TWO_DATA_PATH}")


def load_data() -> dict[str, pd.DataFrame]:
    dataframes = {}
    files = TWENTY_TWENTY_TWO_DATA_PATH.glob("*.csv")

    for file in files:
        fname = file.stem.removeprefix("noahs-")
        dataframes[fname] = pd.read_csv(
            file, dtype=DTYPES_MAP[fname], parse_dates=DATE_COLUMN_MAP[fname]
        )

    return dataframes


def string_to_phone_number(string: str) -> str:
    char_num_map = {
        "a": 2,
        "b": 2,
        "c": 2,
        "d": 3,
        "e": 3,
        "f": 3,
        "g": 4,
        "h": 4,
        "i": 4,
        "j": 5,
        "k": 5,
        "l": 5,
        "m": 6,
        "n": 6,
        "o": 6,
        "p": 7,
        "q": 7,
        "r": 7,
        "s": 7,
        "t": 8,
        "u": 8,
        "v": 8,
        "w": 9,
        "x": 9,
        "y": 9,
        "z": 9,
    }

    phone_number = []

    for char in string:
        phone_number.append(str(char_num_map[char]))

    return "".join(phone_number)
