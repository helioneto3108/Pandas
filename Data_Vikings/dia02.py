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
(df.groupby(by=["TP_ESCOLA", "TP_SEXO"])[["NU_NOTA_MT", "NU_NOTA_CN"]].mean().T)

# %%
(
    df.groupby(by=["TP_ESCOLA"])[["NU_NOTA_MT", "NU_NOTA_CN"]]
    .agg({"NU_NOTA_MT": ["max", "mean"], "NU_NOTA_CN": ["min", "median"]})
    .rename(index={1: "Não informado", 2: "Pública", 3: "Privada"})
)

# %%
# Quais municipios possuem a maior quantidade de inscrito
df.NO_MUNICIPIO_PROVA.value_counts()

# %%
# A media de cada municipio nas provas
(
    df.groupby(by=["NO_MUNICIPIO_PROVA"])[provas]
    .mean()
    .reset_index()
    .rename(
        columns={
            "NO_MUNICIPIO_PROVA": "MUNICIPIO",
            "NU_NOTA_CN": "Média_Ciencia_Natureza",
            "NU_NOTA_CH": "Média_Ciencia_Humanas",
            "NU_NOTA_LC": "Média_Linguagem_Codigo",
            "NU_NOTA_MT": "Média_Matematica",
            "NU_NOTA_REDACAO": "Média_Redação",
        }
    )
    .sort_values(by=["Média_Matematica", "Média_Ciencia_Humanas"], ascending=False)
    .reset_index(drop=True)
)

# %%
df_visao_municipio = (
    df.groupby(by=["NO_MUNICIPIO_PROVA", "CO_MUNICIPIO_PROVA"])[provas]
    .mean()
    .reset_index()
    .rename(
        columns={
            "CO_MUNICIPIO_PROVA": "Cod_IBGE",
            "NO_MUNICIPIO_PROVA": "MUNICIPIO",
            "NU_NOTA_CN": "Média_Ciencia_Natureza",
            "NU_NOTA_CH": "Média_Ciencia_Humanas",
            "NU_NOTA_LC": "Média_Linguagem_Codigo",
            "NU_NOTA_MT": "Média_Matematica",
            "NU_NOTA_REDACAO": "Média_Redação",
        }
    )
    .sort_values(by=["Média_Matematica", "Média_Ciencia_Humanas"], ascending=False)
    .reset_index(
        drop=True
    )  # colocar drop true senão ele joga o index antigo para coluna
)
df_visao_municipio

# %%
df_quantidade_inscritos = (
    df.groupby(by=["NO_MUNICIPIO_PROVA", "CO_MUNICIPIO_PROVA"], as_index=False)[
        "NU_INSCRICAO"
    ]
    .count()
    .rename(
        columns={
            "NO_MUNICIPIO_PROVA": "Município",
            "CO_MUNICIPIO_PROVA": "Cod_IBGE",
            "NU_INSCRICAO": "Quantidade_Inscritos",
        }
    )
    .sort_values(by=["Quantidade_Inscritos"], ascending=False)
    .reset_index(drop=True)
)
df_quantidade_inscritos

# O as_index = false é para falar que não quer colocar aquelas colunas
# como index e sim como um coluna mesmo

# %%
df_quantidade_inscritos["Percentual_Inscritos"] = (
    df_quantidade_inscritos.Quantidade_Inscritos / df.shape[0] * 100
)
df_quantidade_inscritos

# %%
# Verificar se estão todos os inscritos
sum(df_quantidade_inscritos.Quantidade_Inscritos)

# %%
# Verificar se deu 100%
sum(df_quantidade_inscritos.Percentual_Inscritos)

# %%
pd.merge(
    df_visao_municipio,
    df_quantidade_inscritos,
    on="Cod_IBGE",
    how="inner",
)

# %%
df_municipios = pd.merge(
    df_visao_municipio,
    df_quantidade_inscritos,
    on="Cod_IBGE",
    how="inner",
)
df_municipios

# %%
df_municipios = pd.merge(
    df_visao_municipio,
    df_quantidade_inscritos.drop(
        columns=["Município"]
    ),  # Para não ter 2 colunas muncipio
    on="Cod_IBGE",
    how="inner",
)
df_municipios

# %%
df_visao_municipio.merge(df_quantidade_inscritos, how="inner")

# %%
