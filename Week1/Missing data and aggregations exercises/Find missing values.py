import pandas as pd
from data_utils import plot_missing_values

path = pd.read_csv("Week1/Missing data and aggregations exercises/student-mat-missing-data.csv")

plot_missing_values(path)