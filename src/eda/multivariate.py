import pandas as pd
import matplotlib.pyplot as plt




class ChurnInteractionAnalysis:

    def __init__(self, df, target="Churn"):
        self.df = df
        self.target = target

    def crosstab(self, cols, normalize="index"):
        """
        Create crosstab between multiple categorical features and target.
        Input more than two columns
        cols: list of columns (e.g. ["Contract", "InternetService"])
        """
        return pd.crosstab(
            [self.df[c] for c in cols],
            self.df[self.target],
            normalize=normalize # type: ignore
        )

    def plot_crosstab(self,
                      cols,
                      stacked=True,
                      figsize=(12, 6),
                      flatten_index=True,
                      rotate_xticks=45,
                      title=None):


        table = self.crosstab(cols)

        if flatten_index:
            table.index = table.index.map(
                lambda x: " | ".join(map(str, x))
                if isinstance(x, tuple) else x
            )

        ax = table.plot(
            kind="bar",
            stacked=stacked,
            figsize=figsize
        )

        ax.set_ylabel("Churn Rate")
        ax.set_xlabel(" & ".join(cols))
        ax.set_title(title or f"Churn by {' & '.join(cols)}")

        plt.xticks(rotation=rotate_xticks)
        plt.grid(False)
        plt.tight_layout()
        plt.show()

   
