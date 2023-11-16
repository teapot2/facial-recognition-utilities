import os
import logging
from faces import extract_faces_from_database

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)d] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("extract_faces.log"),
    ],
)


if __name__ == "__main__":
    extract_faces_from_database(os.path.join("data", "db"))
