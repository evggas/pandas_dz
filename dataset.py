import pandas as pd

df = pd.read_csv("Dog_Bites_Data.csv")
print(df.head)
print(df.info())
print(df.describe())
