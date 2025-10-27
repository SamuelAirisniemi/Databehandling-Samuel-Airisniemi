import numpy as np
import pandas as pd

df_cities = pd.DataFrame({
    "Kommun": np.array(("Malmö", "Stockholm", "Uppsala", "Göteborg")),
    "Population": np.array((347949, 975551, 233839, 583056))
})

print(f"{df_cities}\n")

df_goteborg = df_cities[df_cities["Kommun"] == "Göteborg"] 
print(f"{df_goteborg}\n")

cities_sorted = df_cities.sort_values(by="Population", ascending=False)
sweden_pop_2020 = 10379295
cities_sorted["Population (%)"] = (cities_sorted["Population"] / sweden_pop_2020 * 100).round(1)

print(f"{cities_sorted.head(3)}\n")
print(f"{cities_sorted}\n")