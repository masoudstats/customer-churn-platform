from src.config.config import load_config
from src.utils.logger import logger


def main():

    logger.info("Loading Configuration...")

    config = load_config()

    logger.info(config)


if __name__ == "__main__":

    main()