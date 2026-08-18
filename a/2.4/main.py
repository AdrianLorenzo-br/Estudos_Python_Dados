import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("a/2.4/titanic.csv")

print(df.head())

print(df.info())

print(df.describe())

print(len(df))
df.drop_duplicates(keep="last", inplace=True)
df.dropna(subset="Cabin", inplace=True)
print(len(df))

