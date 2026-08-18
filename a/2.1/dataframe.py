import pandas as pd

data = {
  "nome" : ["alice", "bob", "charlie", "david"],
  "idade" : [32, 23, 19, 44],
  "cidades" : ["SP", "DF", "RJ", "SC"]
}

df = pd.DataFrame(data)

print(df)

print(df["nome"])

print(df.loc[0, "nome"])

print(df.iloc[1])