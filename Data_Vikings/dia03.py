# %%
import pandas as pd
import numpy as np
import geobr

# Visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

# Set some options in pandas
pd.set_option("display.max_columns", 140)
pd.set_option("display.max_rows", 140)

import warnings

warnings.filterwarnings("ignore")


# %%
def gerar_histograma(
    data_frame,
    variavel,
    bins=30,
    color="red",
    xlabel="Variável",
    ylabel="Frequência",
    titulo="Histograma",
    fontsize=15,
    fontweight="bold",
    figsize=(8, 5),
):
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(data_frame[variavel], bins=bins, color=color)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.set_title(titulo, fontsize=fontsize, fontweight=fontweight)


def gerar_painel_barra(
    data_frame,
    var,
    hue,
    title="",
    title_subplot_1="",
    title_subplot_2="",
    legend_subplot_2="",
    xlabel="Quantidade",
    ylabel="",
    figsize=(12, 6),
):
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    sns.countplot(data=data_frame, y=var, ax=ax[0])
    sns.countplot(data=data_frame, y=var, hue=hue, ax=ax[1])
    ax[0].set(ylabel=ylabel, xlabel=xlabel, title=title_subplot_1)
    ax[1].set(ylabel=ylabel, xlabel=xlabel, title=title_subplot_2)
    ax[1].legend(title=legend_subplot_2)
    fig.suptitle(title)
    fig.tight_layout(pad=4)


def box_plot(data, title, xlabel, ylabel, figsize=(12, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    sns.boxplot(data=data, ax=ax)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)


def boxplot_por_filtro(filtro, data_frame, order=None):
    "Gera um boxplot com filtro para o eixo x e a variável no eixo y."
    provas = ["MATEMATICA", "CIENCIAS_NATUREZA", "LINGUAGENS", "HUMANAS", "REDACAO"]
    filtro_tratado = " ".join(filtro.split("_")).capitalize()

    for prova in provas:
        prova_nome_minusculo = prova.lower()
        fig, ax = plt.subplots(figsize=(15, 5))
        sns.boxplot(x=filtro, y=prova, data=data_frame, ax=ax, order=order)
        ax.set(
            xlabel=filtro_tratado,
            ylabel=f"Nota em {prova_nome_minusculo}",
            title=f"Nota em {prova_nome_minusculo} filtrada por {filtro_tratado}",
        )


def check_missing(df):
    import pandas

    if isinstance(df, pandas.core.frame.DataFrame):
        return (((df.isnull().sum() / df.shape[0]) * 100).round(2)).sort_values(
            ascending=False
        )
    return None


def show_percentage_missing(df):
    import matplotlib.pyplot as plt

    missing = check_missing(df)
    plt.figure(figsize=(10, 20))
    plt.barh(
        y=missing.index,
        width=missing.values,
        color="darkgray",
        height=0.7,
        align="edge",
    )
    plt.xlabel("% of missing values", size=10)
    plt.ylabel("Columns", size=10)
    plt.title(
        "Missing Values", fontdict={"color": "gray", "weight": "bold", "size": 12}
    )
    plt.grid(alpha=0.5)
    plt.show()


def feature_plot_stat(feature, data):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Univariate analysis for {feature}")
    sns.histplot(data[feature], kde=True, ax=ax[0])
    ax[0].set_xlabel("Distribution of " + feature)
    sns.boxplot(y=data[feature], ax=ax[1])
    sns.violinplot(x=data[feature], ax=ax[2])
    fig.tight_layout(pad=3)


def univariate_analysis(features: list, data=pd.DataFrame):
    for feature in features:
        feature_plot_stat(feature, data)


# %%
cols_rename = {
    "Q001": "escolaridade_pai",
    "Q002": "escolaridade_mae",
    "Q003": "ocupacao_pai",
    "Q004": "ocapacao_mae",
    "Q005": "pessoas_residencia",
    "Q006": "renda_mensal_familiar",
    "Q007": "empregada_domestico",
    "Q008": "quantidade_banheiros",
    "Q009": "quantidade_quartos",
    "Q010": "quantidade_carros",
    "Q011": "quantidade_moto",
    "Q012": "geladeira",
    "Q013": "freezer",
    "Q014": "maquina_lavar",
    "Q015": "maquina_secar",
    "Q016": "microondas",
    "Q017": "lava_louca",
    "Q018": "aspirador_po",
    "Q019": "TV",
    "Q020": "DVD",
    "Q021": "TV_assinatura",
    "Q022": "celular",
    "Q023": "telefone_fixo",
    "Q024": "computador",
    "Q025 ": "internet",
    "TP_DEPENDENCIA_ADM_ESC": "TIPO_ESCOLA",
    "TP_LOCALIZACAO_ESC": "LOCALIZACAO_ESCOLA",
    "TP_ESCOLA": "TIPO_ESCOLA",
    "NU_NOTA_MT": "MATEMATICA",
    "NU_NOTA_CN": "CIENCIAS_NATUREZA",
    "NU_NOTA_LC": "LINGUAGENS",
    "NU_NOTA_CH": "HUMANAS",
    "NU_NOTA_REDACAO": "REDACAO",
    "IN_TREINEIRO": "TREINEIRO",
}

cols_drop = [
    "TX_RESPOSTAS_CN",
    "TX_RESPOSTAS_CH",
    "TX_RESPOSTAS_LC",
    "TX_RESPOSTAS_MT",
    "TX_GABARITO_CN",
    "TX_GABARITO_CH",
    "TX_GABARITO_LC",
    "TX_GABARITO_MT",
    "SG_UF_PROVA",
    "CO_PROVA_CH",
    "CO_PROVA_LC",
    "CO_PROVA_MT",
    "CO_PROVA_CN",
]


def editar_estado_civil(estado_civil):
    if estado_civil == 0:
        return "Não Informado"
    elif estado_civil == 1:
        return "Solteiro (a)"
    elif estado_civil == 2:
        return "Casado (a)"
    elif estado_civil == 3:
        return "Divorciado (a)"
    else:
        return "Viúvo (a)"


def editar_sexo(sexo):
    if sexo == "M":
        return "Masculino"
    else:
        return "Feminino"


# def editar_sexo(sexo):
#    if sexo == 'M':
#        return 'Masculino'
#    return 'Feminino'


def editar_cor_raca(cor_raca):
    if cor_raca == 0:
        return "Não informado"
    elif cor_raca == 1:
        return "Branca"
    elif cor_raca == 2:
        return "Preta"
    elif cor_raca == 3:
        return "Parda"
    elif cor_raca == 4:
        return "Amarela"
    else:
        return "Indígena"


def tratar_dados(df):

    # drop de colunas
    df = df.drop(columns=cols_drop)

    # renomear colunas
    df = df.rename(columns=cols_rename)

    # define uma lista das provas que serão analisadas
    provas = ["MATEMATICA", "CIENCIAS_NATUREZA", "LINGUAGENS", "HUMANAS", "REDACAO"]

    # trata colunas categóricas
    df["TP_ESTADO_CIVIL"] = df["TP_ESTADO_CIVIL"].apply(editar_estado_civil)
    df["TP_SEXO"] = df["TP_SEXO"].apply(editar_sexo)
    df["TP_COR_RACA"] = df["TP_COR_RACA"].apply(editar_cor_raca)

    # drop de missing
    df = df.dropna(how="any", subset=provas)

    return df


# %%
df_raw = pd.read_csv("data/dados_enem_2021_BA.csv")
df_raw

# %%
quest = pd.read_csv("data/dados_enem_2021_BA_questoes_socieconomicas.csv")
quest

# %%
df = pd.merge(df_raw, quest, on="NU_INSCRICAO", how="inner")
df

# %%
df = tratar_dados(df)
df

# %%
