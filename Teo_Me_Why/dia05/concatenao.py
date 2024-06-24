# %%
import pandas as pd

# %%
df_01 = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df_01.rename(columns={"valor": "homicidios"}, inplace=True)
df_01

# %%
df_02 = pd.read_csv("../data/ipea/homicidios-por-armas-de-fogo.csv", sep=";")
df_02.rename(columns={"valor": "homicidios-por-armas-de-fogo"}, inplace=True)
df_02

# %%
df_01 = df_01.set_index(["cod", "nome", "período"])
df_02 = df_02.set_index(["cod", "nome", "período"])

# %%
df_01

# %%
df_02

# %%
pd.concat([df_01, df_02], axis=1).reset_index()


# %%
# Jeito otimizado para puxar varios DF
def import_etl(path: str):

    nome = path.split("/")[-1].split(".")[0]

    df = (
        pd.read_csv(path, sep=";")
        .rename(columns={"valor": nome})
        .set_index(["cod", "nome", "período"])
    )

    return df


# %%
import os

# Pacote de sistema operacional
# %%
path = "../data/ipea/"
files = os.listdir(path)
print(files)

# %%
dfs = list()

for i in files:
    dfs.append(import_etl(path + i))

# %%
dfs[0]
# %%
dfs[1]
# %%
dfs[2]

# %%
df_Completo = pd.concat(dfs, axis=1)
df_Completo

# %%
df_Completo = pd.concat(dfs, axis=1).reset_index()
df_Completo

# %%
df_Completo.to_csv("../data/DataFrame_Consolidado.csv", sep=";", index=False)
# Se não colocar index = False ele leva o index para o arquvio
