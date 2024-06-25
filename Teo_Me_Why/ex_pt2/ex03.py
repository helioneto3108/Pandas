# Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:
# Quantidade de linhas
# Quantidade de colunas
# Nome da primeira coluna
# Nome da última coluna

# %%
import pandas as pd

# %%
df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df

# %%
df.shape

# %%
df.columns[0]

# %%
df.columns[-1]
