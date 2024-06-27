# %%
import pandas as pd
import numpy as np

# %%
pd.set_option("display.max_columns", 100)
df = pd.read_csv("data/dados_enem_2021_BA.csv")
df

# %%
df.shape

# %%
df[df["TP_SEXO"] == "M"].NU_NOTA_MT.mean()

# %%
df[df["TP_SEXO"] == "F"].NU_NOTA_MT.mean()

# %%
df[df["TP_SEXO"] == "M"]["NU_NOTA_MT"].mean()

# %%
provas = df.columns[
    (df.columns.str.contains("NOTA")) & (~df.columns.str.contains("COMP"))
]
provas

# %%
idCandidato = ["NU_INSCRICAO"]
idCandidato

# %%
(df[df["TP_SEXO"] == "M"][provas].agg([np.min, np.mean, np.median, np.max]))

# %%
(df[df["TP_SEXO"] == "M"][provas].agg([np.min, np.mean, np.median, np.max]).T)

# %%
(df[df["TP_SEXO"] == "F"][provas].agg([np.min, np.mean, np.median, np.max]).T)

# %%
df["TP_SEXO"].value_counts()

# %%
# Quem foi o aluno que tirou a maior nota em matematica
df[df["NU_NOTA_MT"] == df["NU_NOTA_MT"].max()]

# %%
# Tirando os NAs e zeros para calcular
mask_1 = df["NU_NOTA_MT"].notna()
mask_2 = df["NU_NOTA_MT"] != 0
subset_mat = df[mask_1 & mask_2]
subset_mat

# %%
subset_mat.NU_NOTA_MT.agg(["min", "mean", "median", "max"])

# %%
# Media das colunas (De cada materia)
df[provas].mean(axis=0)

# %%
# Média da linhas (Média do estudante)
df[provas].mean(axis=1)

# %%
# Calculando porcentagens de NAs em cada coluna
(df.isna().sum() / df.shape[0] * 100).sort_values(ascending=False)

# %%
df_copy = df.copy()
df_copy["Mean"] = df[provas].mean(axis=1)
df_copy

# %%
df_copy["Mean"].mean()

# %%
df_copy["Mean"].quantile(0.75)

# %%
df_copy["Mean"].max()

# %%
# Groupby
# Vendo a proporção do sexo
df.groupby(by=["TP_SEXO"])["NU_INSCRICAO"].count()

# %%
# Agora agrupando junto com a escola
df.groupby(by=["TP_SEXO", "TP_ESCOLA"])["NU_INSCRICAO"].count()

# %%
# Desempenho em matematica por tipo de escola
df.groupby(by=["TP_ESCOLA"])["NU_NOTA_MT"].mean()

# %%
df.groupby(by=["TP_ESCOLA"])[["NU_NOTA_MT", "NU_NOTA_CN"]].mean()

# %%
(
    df.groupby(by=["TP_ESCOLA"])[["NU_NOTA_MT", "NU_NOTA_CN"]]
    .agg(["min", "mean", "median"])
    .T
)

# %%
df.groupby(by=["TP_ESCOLA", "TP_SEXO"])[["NU_NOTA_MT", "NU_NOTA_CN"]].mean().T

# %%
