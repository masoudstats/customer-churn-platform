import pandas as pd
import matplotlib.pyplot as plt





class CorrelationAnalysis:

    def __init__(self, df):
        self.df = df

    def correlation(self):
        """
        Return correlation matrix of numeric features.
        """
        num = self.df.select_dtypes(include="number")
        return num.corr()

    def plot_correlation(self, figsize=(8, 6), cmap="viridis", show_values=False):
        """
        Plot correlation heatmap.
        """

        corr = self.correlation()

        fig, ax = plt.subplots(figsize=figsize)

        cax = ax.imshow(corr, cmap=cmap)

        # axis labels
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.columns)))

        ax.set_xticklabels(corr.columns, rotation=90)
        ax.set_yticklabels(corr.columns)

        # color bar
        fig.colorbar(cax)

        # optional: show values inside heatmap
        if show_values:
            for i in range(len(corr.columns)):
                for j in range(len(corr.columns)):
                    ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                            ha="center", va="center",
                            color="white", fontsize=8)

        ax.set_title("Correlation Matrix")
        plt.tight_layout()
        plt.show()

        return corr