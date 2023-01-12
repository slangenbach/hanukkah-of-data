import logging

from hanukkah_of_data.utils import download_data, extract_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Bootstrapping project")
    download_data()
    extract_data()
    logger.info("Finished bootstrapping project")
