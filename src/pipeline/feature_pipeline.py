from src.data.data_loader import load_data
from src.features.split import split_data
from src.features.encoding import encode_target
from src.features.pipline import build_transformer
# from src.features.selection import select_features
# from src.features.importance import feature_importance
from src.features.save_transformer import save_transformer_encoder




def run():

    df = load_data()

    # Split data to train and test
    X_train, X_test, y_train, y_test = split_data(df)

    X_train = X_train.drop(columns=["customerID"])
    X_test = X_test.drop(columns=["customerID"])


    # Encode Target
    y_train, y_test, target_encoder = encode_target(y_train, y_test)


    # Build Transformer
    categorical_columns = X_train.select_dtypes(include="str").columns.tolist()
    numerical_columns = X_train.select_dtypes(exclude="object").columns.tolist()

    transformer = build_transformer(categorical_columns, numerical_columns)

    # Fit , Transform
    X_train = transformer.fit_transform(X_train)

    X_test = transformer.transform(X_test)


    # # Feature Selection
    # selector = select_features()

    # # Fit, selector
    # X_train = selector.fit_transform(X_train, y_train)

    # X_test = selector.transform(X_test)


    # # Feature Importance
    # selected_columns = transformer.get_feature_names_out()[selector.get_support()]

    # importance = feature_importance(X_train, y_train, selected_columns)


    # Save Transformer and encoder
    save_transformer_encoder(transformer=transformer, target_encoder=target_encoder, main_path='artifacts/')




if __name__ == "__main__":

    run()