# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
df["Points_Double"] = df["Points"] * 2
df

# %%
df["Points_ratio"] = df["Points_Double"] / df["Points"]
df

# %%
df["constante"] = 1
df

# %%
df["Points_log"] = np.log(df["Points"])
df

# %%
# Fazendo de forma sequencial, ou seja, uma linha por vez. Isso é considerado demorado
nomes_altas = list()
for i in df["Name"]:
    nomes_altas.append(i.upper())

df["Nome_alta_sequencial"] = nomes_altas
df

# %%
# Fazendo de forma vetorial, ou seja, todas as linhas ao mesmo todo
df["Nome_alta_vetorial"] = df["Name"].str.upper()
df


# %%
def get_first(nome: str):
    return nome.split("_")[0]


# %%
# Comando utilizado para aplicar uma função em todas as linhas da minha serie
df["Name"].apply(get_first)

# %%
# Outro jeito de aplicar, utilizando a funcao lambda
df["Name"].apply(lambda nome: nome.split("_")[0])


# %%
def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "médio"
    else:
        return "alto"


df["Faixas_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%
# Pegando os tres ultimos caracteres do "UUID"
df["UUID"].apply(lambda x: x[-3:])

# %%
data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1, 30, 10, 45],
    "valor": [100, 2000, 15, 500],
    "frequencia": [2, 5, 1, 15],
}

df_crm = pd.DataFrame(data)
df_crm


# %%
def rfv(row):

    nota = 0

    if row["recencia"] <= 10:
        nota += 10
    elif 10 < row["recencia"] <= 30:
        nota += 5
    elif row["recencia"] > 30:
        nota += 0

    if row["valor"] > 1000:
        nota += 10
    elif 100 <= row["valor"] < 1000:
        nota += 5
    elif row["valor"] < 100:
        nota += 0

    if row["frequencia"] > 10:
        nota += 10
    elif 5 <= row["frequencia"] < 10:
        nota += 5
    elif row["frequencia"] < 5:
        nota += 0

    return nota


# %%
# axis = 1, significa que ele estará fazendo o apply recebendo a linha, para cada linha
# Ou seja, nesse caso os valores que irão substituir os parametros serão os valores da linha
# axis = 0, que é o default é para cada coluna
# Ou seja, nesse caso os valores que irão substituir os parametros serão os valores da coluna
df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%

df_crm.iloc[0]
# %%
