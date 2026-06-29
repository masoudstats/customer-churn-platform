from src.data.data_loader import load_data

from src.data.data_validator import validate_columns

from src.data.preprocessing import *

from src.data.save_data import save_processed


def run():

    df = load_data()

    validate_columns(df)

    df = remove_duplicates(df)

    check_missing(df)

    df = fix_total_charge(df)

    save_processed(df)


if __name__ == "__main__":

    run()