# %%
import pandas as pd

# %%
df = pd.read_csv("../data/DataFrame_Consolidado.csv", sep=";")
df

# %%
df = df.set_index(["cod", "nome", "período"])
df

# %%
# Utilizado, pois é melhor para armazenamento tabelas com mais linhas do que colunas
df.stack()

# %%
df.stack().reset_index()

# %%
df_stack = (
    df.stack().reset_index().rename(columns={"level_3": "Tipo_Homicidio", 0: "Valor"})
)
df_stack

# %%
df_stack.set_index(["cod", "nome", "período", "Tipo_Homicidio"]).unstack()

# %%
df_unstack = (
    df_stack.set_index(["cod", "nome", "período", "Tipo_Homicidio"])
    .unstack()
    .reset_index()
)
df_unstack

# %%
df_unstack.columns

# %%
df_unstack["cod"]

# %%
df_unstack["Valor"]

# %%
df_unstack["Valor"].columns

# %%
homicidios = df_unstack["Valor"].columns.tolist()
homicidios

# %%
df_unstack.columns = ["cod", "nome", "período"] + homicidios
df_unstack

# %%
# Outro jeito de fazer
homicidios = df_unstack["Valor"].columns.tolist()
homicidios

identificadores = df_unstack.columns.droplevel(1).tolist()[:3]
# Pegando as primeiras 3 colunas

df_unstack.columns = identificadores + homicidios
df_unstack
