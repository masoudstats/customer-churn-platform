# from src.config.config import load_config
# from src.utils.logger import logger

from src.data.data_loader import load_data
from src.data.data_validator import validate_columns


def main():

    # logger.info("Loading Configuration...")

    # config = load_config()

    # logger.info(config)


    df = load_data()

    print(df.head())

    validate_columns(df) 

if __name__ == "__main__":

    main()