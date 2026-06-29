import pandas as pd
import matplotlib.pyplot as plt




class ChurnAnalysis:

    def __init__(self, df, target="Churn"):
        self.df = df
        self.target = target

    def churn_rate(self, column):
        """
        Return normalized churn rate table.
        """
        return pd.crosstab(
            self.df[column],
            self.df[self.target],
            normalize="index"
        )

    def plot_churn_rate(self, column, stacked=True, figsize=(8, 5)):
        """
        Plot churn rate for a categorical feature.
        """
        table = self.churn_rate(column)

        ax = table.plot.bar(
            stacked=stacked,
            figsize=figsize
        )

        ax.set_title(f"Churn Rate by {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Percentage")
        ax.grid(False)

        plt.tight_layout()
        plt.show()

    def summary(self, column):
        """
        Return count and churn rate together.
        """
        counts = self.df[column].value_counts().sort_index()
        rates = self.churn_rate(column)

        return counts.to_frame("Count").join(rates)
    

