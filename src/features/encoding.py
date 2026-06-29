from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def encode_target(y_train, y_test):

    encoder = LabelEncoder()

    y_train = encoder.fit_transform(y_train)

    y_test = encoder.transform(y_test)

    return y_train, y_test, encoder




def one_hot():

    return OneHotEncoder(

        handle_unknown="ignore",

        sparse_output=False

    )
