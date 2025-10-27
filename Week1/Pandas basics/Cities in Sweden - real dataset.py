import pandas as pd 

df = pd.read_excel("C:/Users/samue/Desktop/komtopp50_2020.xlsx")
df = df.iloc[6:]

print(df.head(5))