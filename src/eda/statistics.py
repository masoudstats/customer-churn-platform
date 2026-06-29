from scipy.stats import chi2_contingency, ttest_ind
import pandas as pd





class StatisticalAnalysis:

    def __init__(self, df, target="Churn"):
        self.df = df
        self.target = target

    def chi_square(self, column):
        """
        Chi-Square test for categorical feature.
        """

        table = pd.crosstab(
            self.df[column],
            self.df[self.target]
        )

        chi2, p_value, dof, expected = chi2_contingency(table)

        return {
            "chi2": chi2,
            "p_value": p_value,
            "dof": dof,
            "expected": expected
        }

    def t_test(self, column, equal_var=False):
        """
        Independent t-test for numerical feature.
        """

        group1 = self.df[self.df[self.target] == "Yes"][column]
        group2 = self.df[self.df[self.target] == "No"][column]

        stat, p_value = ttest_ind(
            group1,
            group2,
            equal_var=equal_var,
            nan_policy="omit"
        )

        return {
            "t_statistic": stat,
            "p_value": p_value
        }