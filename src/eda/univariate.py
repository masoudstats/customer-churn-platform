import pandas as pd


def numerical_summary(df):

    return df.describe().T




def categorical_summary(df):

    cat_cols = df.select_dtypes(include="object").columns

    summaries = {}

    for col in cat_cols:

        summaries[col] = df[col].value_counts()

    return summaries



def missing_summary(df):

    return df.isnull().sum().sort_values(ascending=False)



def unique_summary(df):

    return df.nunique()



def datatype_summary(df):

    return df.dtypes