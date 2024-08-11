# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("data/dados_enem_2021_BA.csv")
df

# %%
# Qual a proporção entre os gêneros?
df["TP_SEXO"].value_counts() / df.shape[0] * 100

# %%
# Qual a distribuição de frequência do alunos pelo tipo de escola
(
    df["TP_ESCOLA"]
    .map({1: "Não respondeu", 2: "Públcia", 3: "Privada"})
    .value_counts()
    .plot(
        kind="pie",
        title="distribuição de frequência do alunos pelo tipo de escola",
        autopct="%.2f",  # Para colocar o valor no gráfico
    )
)

# %%
# Tirando os 0
df_subset = df[df.NU_NOTA_MT != 0]
df_subset

# %%
# Qual o desempenho de matematica por cada tipo de escola
(
    df_subset[df_subset["TP_ESCOLA"] == 2].NU_NOTA_MT.agg(
        ["min", "mean", "median", "max"]
    )
)

# %%
(
    df_subset[df_subset["TP_ESCOLA"] == 3].NU_NOTA_MT.agg(
        ["min", "mean", "median", "max"]
    )
)

# %%
