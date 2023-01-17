import argparse
import logging

from hanukkah_of_data.utils import YEARS_MAP, download_data, extract_data

logging.basicConfig(level=logging.INFO, style="{", format="{levelname}: {message}")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download and extract data for Hanukkah of Data"
    )
    parser.add_argument("year", choices=[year for year in YEARS_MAP.keys()])
    args = parser.parse_args()

    logger.info(f"Bootstrapping Hanukkah of Data for year {args.year}")
    download_data(year=args.year)
    extract_data(year=args.year)
    logger.info("Finished bootstrapping")
