import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_values(df: pd.DataFrame) -> None:
    missing_counts = df.isnull().sum()
    missing_counts = missing_counts[missing_counts > 0].sort_values(ascending = False)

    if missing_counts.empty:
        print("No missing values found in the DataFrame.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=missing_counts.index, y=missing_counts.values, palette="viridis")
    plt.title("Missing Values per Column")
    plt.xlabel("Columns")
    plt.ylabel("Number of Missing Values")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
