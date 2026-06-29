from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def feature_importance(X, y, feature_names):

    model = RandomForestClassifier(random_state=42)

    model.fit(X,y)

    importance = pd.DataFrame({"Feature":feature_names, 
                               "Importance":model.feature_importances_}
                            )

    return importance.sort_values("Importance",ascending=False)