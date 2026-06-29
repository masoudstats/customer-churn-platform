from src.utils.logger import logger


def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    logger.info(f"Removed {before-after} duplicates")

    return df



def check_missing(df):

    missing = df.isna().sum()

    logger.info(missing)

    return missing



def fix_total_charge(df):

    # replace "" with None type
    df["TotalCharges"] = df["TotalCharges"].replace(" ", None).astype(float)

    # Handling NaN values
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    logger.info("'TotalCharges' is processed by filling NaN values")

    return df



def print_types(df):

    print(df.dtypes)