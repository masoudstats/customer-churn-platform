from pathlib import Path

from src.config.config import load_config

config = load_config()


def save_processed(df):

    path = Path(config["paths"]["processed_data"])

    path.mkdir(exist_ok=True)

    output = path / "processed.csv"

    df.to_csv(output, index=False)