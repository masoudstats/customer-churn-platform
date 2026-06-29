from sklearn.compose import ColumnTransformer

from src.features.encoding import one_hot
from src.features.scaling import scaler



def build_transformer(categorical_columns, numerical_columns):

    transformer = ColumnTransformer(

        transformers = [
            ("cat", one_hot(), categorical_columns),

            ("num", scaler(), numerical_columns)
        ]

    )

    return transformer