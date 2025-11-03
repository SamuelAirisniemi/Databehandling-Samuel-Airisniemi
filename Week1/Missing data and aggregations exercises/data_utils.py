import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_values(df):
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0]

    if missing_counts.empty:
        print("No missing values found in the DataFrame.")
        return

    order = missing_counts.index.tolist()

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=missing_counts.index,
        y=missing_counts.values,
        order=order
    )
    plt.title("Null Values")
    plt.xlabel("Column")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()