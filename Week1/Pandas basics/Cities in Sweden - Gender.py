import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

male = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Män")
male.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
male["Kön"] = "Man"

female = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Kvinnor")
female.columns = ["Rang 2020", "Rang 2019", "Kommun", "Folkmängd 2020", "Folkmängd 2019", "Förändring"]
female["Kön"] = "Kvinna"

df_all = pd.concat([male, female], ignore_index = True)

total = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx", header = 6, sheet_name = "Totalt", usecols = "C:F")
total.columns = ["Kommun", "Total pop 2020", "Total pop 2019", "Total förändring"]

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

gender_totals = merged.groupby("Kön")["Folkmängd 2020"].sum()

plt.figure(figsize=(6, 6))
plt.pie(
    gender_totals,
    labels=gender_totals.index,
    autopct="%.1f%%",
    startangle=90,
    colors=["steelblue", "darkorange"]
)
plt.title("Könsfördelning i Sverige 2020")
plt.legend(title = "Kön")
plt.show()

pivot = merged.pivot(index="Kommun", columns="Kön", values="Folkmängd 2020").reset_index()

pivot["Diff"] = pivot["Man"] - pivot["Kvinna"]
pivot["PercentDiff"] = (pivot["Diff"] / (pivot["Man"] + pivot["Kvinna"])) * 100

top5_diff = pivot.reindex(pivot["PercentDiff"].abs().sort_values(ascending=False).index).head(5)

df_melted = top5_diff.melt(
    id_vars=["Kommun", "Diff", "PercentDiff"],
    value_vars=["Man", "Kvinna"],
    var_name="Kön",
    value_name="Folkmängd 2020"
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=df_melted,
    x="Kommun", y="Folkmängd 2020",
    hue="Kön",
    palette={"Man": "steelblue", "Kvinna": "darkorange"}
)

plt.title("De 5 kommunerna med störst könsskillnad i procent (2020)")
plt.xlabel("Kommun")
plt.ylabel("Antal invånare 2020")
plt.legend(title="Kön")
plt.tight_layout()
plt.show()

totalt = pd.read_excel(
    "C:/Users/samue/Desktop/komtopp50_2020.xlsx",
    header=6,
    sheet_name="Totalt",
    usecols="C:F"
)

totalt.columns = ["Kommun", "Total_2020", "Total_2019", "Procent_forandring"]
top5 = totalt.sort_values("Procent_forandring", ascending=False).head(5)

plt.figure(figsize=(8, 6))
sns.barplot(
    data=top5,
    x="Kommun",
    y="Procent_forandring"
)
plt.title("Top 5 kommuner med störst procentuell befolkningstillväxt (2019–2020)")
plt.xlabel("Kommun")
plt.ylabel("Tillväxt (%)")
plt.tight_layout()
plt.show()