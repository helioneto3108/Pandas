# %%
import pandas as pd

# %%

data = {
    "nome": ["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2],
}

# %%
data["idade"][0]

# %%
df = pd.DataFrame(data)
df

# %%
df["idade"]

# %%
df["idade"].iloc[0]

# %%
df.iloc[0]

# %%
df.index = [3, 2, 1, 0]
df

# %%
df["idade"][0]

# %%
df["idade"].iloc[0]

# %%
# Mesma coisa que df['idade'][0], pois loc procura por indice
# Ou seja, o .loc pode ser dispensado já que o default é procurar por indice
df["idade"].loc[0]

# %%
df.index

# %%
df.columns

# %%
df.info()

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
df.describe()

# %%
# Adicionando mais uma coluna e colocando as dimensões
df["pesos"] = [80, 53, 65, 72]

df.describe()

# %%
sumario = df.describe()
sumario["pesos"]

# %%
sumario["pesos"]["mean"]

# %%
# Mostra a quantidade de linhas que vc mandar, partindo da primeira
df.head(2)

# %%
# Mostra a quantidade de linhas que vc mandar, partindo da ultima
df.tail(3)

# %%
