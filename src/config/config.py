from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parents[2]


CONFIG_PATH = BASE_DIR / "configs" / "config.yaml"


def load_config():

    with open(CONFIG_PATH, "r") as file:

        config = yaml.safe_load(file)

    return config