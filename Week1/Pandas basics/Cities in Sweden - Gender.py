import pandas as pd
import matplotlib.pyplot as plt

male = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Män")
male.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
male["Kön"] = "Man"

#print(f"{male.head(5)}\n")

female = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Kvinnor")
female.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
female["Kön"] = "Kvinna"

#print(f"{female.head(5)}")

df_all = pd.concat([male, female], ignore_index = True)
#print(df_all)

total = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Totalt", usecols = "C:F")
total.columns = ["Kommun", "Total pop 2020", "Total pop 2019", "Total förändring"]
#print(f"{total.head(5)}")

merged = pd.merge(
    df_all,
    total,
    on = "Kommun",
    how = "left"
)

merged = merged[[
    "Kommun",
    "Folkmängd 2020",
    "Folkmängd 2019",
    "Förändring",
    "Kön",
    "Total pop 2020",
    "Total pop 2019",
    "Total förändring"
]]

merged_sorted = merged.sort_values(by = "Total pop 2020", ascending = False)

top_kommuner = merged_sorted["Kommun"].unique()[:5]
resultat = merged_sorted[merged_sorted["Kommun"].isin(top_kommuner)]
#print(resultat)

top10 = merged_sorted["Kommun"].unique()[:10]
bottom10 = merged_sorted["Kommun"].unique()[-10:]

df_top10 = merged[merged["Kommun"].isin(top10)]
df_bottom10 = merged[merged["Kommun"].isin(bottom10)]

pivot_top = df_top10.pivot(index="Kommun", columns="Kön", values="Folkmängd 2020")
pivot_top = pivot_top.reindex(top10)

pivot_bottom = df_bottom10.pivot(index="Kommun", columns="Kön", values="Folkmängd 2020")
pivot_bottom = pivot_bottom.reindex(bottom10)


fig, axes = plt.subplots(1, 2, figsize=(16, 4))

pivot_top.plot(kind="barh", ax=axes[0], color={"Man": "steelblue", "Kvinna": "darkorange"})
axes[0].set_title("Populationen i 10 största städerna i Sverige fördelat i kön")
axes[0].set_xlabel("Folkmängd 2020")
axes[0].invert_yaxis()

pivot_bottom.plot(kind="barh", ax=axes[1], color={"Man": "steelblue", "Kvinna": "darkorange"})
axes[1].set_title("Populationen i 10 minsta städerna i Sverige fördelat i kön")
axes[1].set_xlabel("Folkmängd 2020")
axes[1].invert_yaxis()

plt.tight_layout()
plt.show()