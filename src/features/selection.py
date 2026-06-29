from sklearn.feature_selection import SelectKBest, mutual_info_classif



def select_features(k=20):

    return SelectKBest(score_func=mutual_info_classif, k=k)