import matplotlib.pyplot as plt


def plot_histogram(df,column):

    plt.figure(figsize=(6,4))

    plt.hist(df[column], bins=30, edgecolor='black')
    
    plt.title(f"Hist of '{column}'")

    plt.tight_layout()
    plt.grid(False)
    
    plt.show()




def plot_bar(df,column):

    df[column].value_counts().plot.bar()

    plt.title(column)

    plt.tight_layout()

    plt.show()



def plot_box(df,column):

    plt.boxplot(df[column])

    plt.title(column)

    plt.show()