from pathlib import Path
import pandas as pd

from src.config.config import load_config
from src.utils.logger import logger

config = load_config()


def load_data():

    raw_path = Path(config["paths"]["raw_data"]) / "Telco-Customer-Churn.csv"

    logger.info(f"Loading data from {raw_path}")

    df = pd.read_csv(raw_path)

    logger.info(f"Dataset Shape : {df.shape}")

    return df