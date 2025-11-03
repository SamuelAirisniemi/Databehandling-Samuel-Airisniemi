import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Totalt")
df.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]

df = df.sort_values(by="Folkmängd 2020", ascending=False).reset_index(drop = True)

total_2019 = df["Folkmängd 2019"].sum()
total_2020 = df["Folkmängd 2020"].sum()

print(f"{df.head(5)}\n")
print(f"Populationen i Sverige 2020: {total_2020}")
print(f"Populationen i Sverige 2019: {total_2019}")

top5 = df.head(5)
bottom5 = df.tail(5)

fig, axes = plt.subplots(1, 2, figsize = (14, 6))

axes[0].bar(top5["Kommun"], top5["Folkmängd 2020"], color = "steelblue")
axes[0].set_title("Sveriges 5 största kommuner 2020")
axes[0].set_ylabel("Folkmängd 2020")
axes[0].tick_params(axis = "x", rotation = 45)

axes[1].bar(bottom5["Kommun"], bottom5["Folkmängd 2020"], color = "darkorange")
axes[1].set_title("Sveriges 5 minsta kommuner 2020")
axes[1].set_ylabel("Folkmängd 2020")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()