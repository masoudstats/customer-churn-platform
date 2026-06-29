from src.utils.logger import logger


EXPECTED_COLUMNS = [
    'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',

    'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',

    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV','StreamingMovies',
    
    'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'
]


def validate_columns(df):

    missing = set(EXPECTED_COLUMNS) - set(df.columns)

    if len(missing) > 0:

        raise Exception(f"Missing Columns : {missing}")

    logger.info("Column Validation Passed")