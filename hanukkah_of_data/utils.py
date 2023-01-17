import logging
import urllib.request
from zipfile import ZipFile

import pandas as pd

from hanukkah_of_data.constants import DATE_COLUMN_MAP, DTYPES_MAP, YEARS_MAP


def download_data(year: str) -> None:
    data_path = YEARS_MAP[year]["data_path"]
    url = YEARS_MAP[year]["url"]

    data_path.mkdir(exist_ok=True)
    if not data_path.joinpath("data.zip").exists():
        logging.info(f"Downloading data from {url} to {data_path}/data.zip")
        urllib.request.urlretrieve(url, data_path.joinpath("data.zip"))
    else:
        logging.info(f"Data has already been downloaded to {data_path}/data.zip")


def extract_data(year: str) -> None:
    data_path = YEARS_MAP[year]["data_path"]
    pwd = YEARS_MAP[year]["pwd"]

    if data_path.joinpath("data.zip").exists():
        if not list(data_path.glob("*.csv")):
            logging.info(f"Extracing data.zip to {data_path}")
            with ZipFile(data_path.joinpath("data.zip")) as f:
                f.extractall(
                    path=data_path,
                    pwd=str.encode(pwd),
                )
        else:
            logging.info("Data has already been extracted.")
    else:
        logging.warning(f"File 'data.zip' does not exist in {data_path}")


def load_data(year: str = "5777") -> dict[str, pd.DataFrame]:
    data_path = YEARS_MAP[year]["data_path"]
    dataframes = {}
    files = data_path.glob("*.csv")

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
