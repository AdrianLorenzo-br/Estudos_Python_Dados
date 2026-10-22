import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("Aulas/Modelagem/Md1/Cópia de tabela_vendas_ZePequeno.xlsx - Vendas_2025.csv")

df["Canal"] = df["Canal"].fillna("Desconhecido")

df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y %H:%M:%S", errors="coerce")
df["Mes"] = df["Data"].dt.to_period("M")
vendas_mes = df.groupby("Mes")
Canais = df["Canal"].value_counts().head(3)
Data = df["Data"]

print(vendas_mes)

plt.plot(Canais[0], vendas_mes,)
plt.plot(Canais[1], vendas_mes,)
plt.show()
