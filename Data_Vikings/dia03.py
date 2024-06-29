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


### define uma lista das provas que serão analisadas
provas = ["MATEMATICA", "CIENCIAS_NATUREZA", "LINGUAGENS", "HUMANAS", "REDACAO"]

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
df[provas]

# %%
# filtra os dados para a condição de Treineiro
treineiro = df.query("TREINEIRO == 1")

# %%
# Criando o plot
var_idade = "TP_FAIXA_ETARIA"

fig, ax = plt.subplots(3, 2, figsize=(15, 12))
# Titulo da figura
fig.suptitle(
    "Perfil etário dos inscritos no ENEM",
    fontsize=20,  # Tamanho da fonte
    fontweight="bold",
)  # Estilo da fonte
# Inserir um gráfio de hist no eixo 0,0
ax[0, 0].hist(df[var_idade], bins=30)  # Bins é a quantidade de classe
ax[0, 0].set(xlabel="Classe_Idade", ylabel="Frequência")
ax[0, 0].set_title("Inscritos Gerais")
# insere um histograma para a idade dos treineiros no eixo ax[0,1]
ax[0, 1].hist(treineiro[var_idade], bins=30)
# altera os labels do eix[0,1]
ax[0, 1].set(xlabel="Classe_Idade", ylabel="Frequência")
ax[0, 1].set_title("Treineiro")
# distribuição da idade dos inscritos gerais no eixo ax[1,0] e altera os labels
sns.distplot(df[var_idade], ax=ax[1, 0])
ax[1, 0].set(xlabel="Idade", ylabel="Frequência", title="Inscritos gerais")
# distribuição da idade dos treineiros nos eixo ax[1,1] e altera os labels
sns.distplot(treineiro[var_idade], ax=ax[1, 1])
ax[1, 1].set(xlabel="Idade", ylabel="Frequência", title="Treineiro")
# boxplot da idade no eixo ax[2,0] e altera os labels
sns.boxplot(data=df, x=var_idade, ax=ax[2, 0])
ax[2, 0].set(xlabel="Idade", title="Inscritos gerais")
# boxplot da idade no eixo ax[2,1] e altera os labels
sns.boxplot(data=treineiro, x=var_idade, ax=ax[2, 1])
ax[2, 1].set(xlabel="Idade", title="Treineiro")
plt.tight_layout(pad=4)

# %%
# Perfil de genero
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x="TP_SEXO", ax=ax)
ax.set(xlabel="Sexo", ylabel="Quantidade", title="Distribuição de gênero")

# %%
fig, ax = plt.subplots(1, 2, figsize=(10, 6))
sns.countplot(data=df, y="TP_ESTADO_CIVIL", ax=ax[0])
sns.countplot(data=df, y="TP_ESTADO_CIVIL", hue="TP_SEXO", ax=ax[1])
ax[0].set(ylabel="Estado Civil", xlabel="Quantidade", title="Estado civil")
ax[1].set(ylabel="Estado Civil", xlabel="Quantidade", title="Estado civil por gênero")
ax[1].legend(title="Gênero")
fig.suptitle("Estado civil dos inscritos")
fig.tight_layout(pad=4)

# %%
# Cor, raça e nacionalidade
gerar_painel_barra(
    df,
    "TP_COR_RACA",
    "TP_SEXO",
    title="Perfil de cor e raça dos inscritos",
    title_subplot_1="Cor/raça",
    title_subplot_2="Cor/raça por gênero",
    legend_subplot_2="Gênero",
    ylabel="Cor/raça",
)

# %%
# Analise univariada das provas
### define uma lista das provas que serão analisadas
univariate_analysis(provas, data=df)

# %%
# Mapa de calor das provas
fig, ax = plt.subplots()
# Fazendo o calculo de correlação entre as provas
cor_provas = df[provas].corr()
# Plotando o mapa de calor com as correlações
sns.heatmap(cor_provas, annot=True, cmap="Blues", ax=ax, fmt=".2f")

# %%
fig, ax = plt.subplots(figsize=(10, 10))
sns.boxplot(data=df[provas], ax=ax)

# %%
renda_ordenada = df["renda_mensal_familiar"].unique()
renda_ordenada.sort()
boxplot_por_filtro("renda_mensal_familiar", df, renda_ordenada)

# %%
df_visao_municipio = (
    df_raw.query("NU_NOTA_MT != 0 ")
    .groupby(by=["NO_MUNICIPIO_PROVA", "CO_MUNICIPIO_PROVA"], as_index=False)[
        "NU_NOTA_MT"
    ]
    .agg([np.min, np.mean, np.median, np.max])
    .reset_index(drop=False)
    .rename(
        columns={
            "CO_MUNICIPIO_PROVA": "COD_IBGE",
            "NO_MUNICIPIO_PROVA": "Município",
            "min": "Mínimo_MT",
            "mean": "Média_MT",
            "median": "Mediana_MT",
            "max": "Máximo_MT",
        }
    )
    .sort_values(by=["Máximo_MT", "Média_MT", "Mediana_MT"], ascending=False)
    .reset_index(drop=True)
)


df_quantidade_inscritos = (
    df_raw.groupby(by=["NO_MUNICIPIO_PROVA", "CO_MUNICIPIO_PROVA"], as_index=False)[
        "NU_INSCRICAO"
    ]
    .count()
    .rename(
        columns={
            "NO_MUNICIPIO_PROVA": "Município",
            "CO_MUNICIPIO_PROVA": "COD_IBGE",
            "NU_INSCRICAO": "Quantidade_inscritos",
        }
    )
    .sort_values(by=["Quantidade_inscritos"], ascending=False)
    .reset_index(drop=True)
)

total = df_quantidade_inscritos.Quantidade_inscritos.sum()

df_quantidade_inscritos["Percentual_inscritos"] = (
    df_quantidade_inscritos.Quantidade_inscritos / total * 100
).round(2)

df_quantidade_inscritos["NU_ANO"] = 2021

df_municipio = pd.merge(
    df_visao_municipio.drop(columns=["Município"]),
    df_quantidade_inscritos,
    on="COD_IBGE",
    how="inner",
)

# %%
(
    df_municipio.nlargest(n=20, columns="Quantidade_inscritos")
    .set_index("Município")["Quantidade_inscritos"]
    .plot(kind="barh")
)

# %%
# Analise espacial
# municípios BA
ba_muni = geobr.read_municipality(code_muni="BA", year=2010)

# %%
# plot
fig, ax = plt.subplots(figsize=(5, 5), dpi=150)

ba_muni.plot(facecolor="#2D3E50", edgecolor="#FEBF57", linewidth=0.3, ax=ax)

ax.set_title("Municípios BA, 2010", fontsize=4)
ax.axis("off")

# %%
ba_muni.head(1)

# %%
df_spatial_enem = ba_muni.merge(
    df_municipio, left_on="code_muni", right_on="COD_IBGE", how="left"
)

# %%
# verifica volumetria
df_municipio.shape, ba_muni.shape, df_spatial_enem.shape

# %%
df_spatial_enem.isna().sum()

# %%
df_spatial_enem = df_spatial_enem.fillna(-999)

# %%
df_spatial_enem.isna().sum()

# %%
plt.rcParams.update({"font.size": 5})

fig, ax = plt.subplots(figsize=(4, 4), dpi=150)

df_spatial_enem.plot(
    column="Quantidade_inscritos",
    cmap="Blues",
    legend=True,
    edgecolor="gray",
    linewidth=0.3,
    legend_kwds={
        "label": "Quantidade de inscritos",
        "orientation": "vertical",
        "shrink": 0.3,
    },
    ax=ax,
)

ax.set_title("Inscritos por município no ENEM - BA, 2021")
ax.axis("off")

# %%
plt.rcParams.update({"font.size": 5})

fig, ax = plt.subplots(figsize=(4, 4), dpi=150)

df_spatial_enem.plot(
    column="Máximo_MT",
    cmap="Blues",
    legend=True,
    edgecolor="gray",
    linewidth=0.3,
    legend_kwds={
        "label": "Quantidade de inscritos",
        "orientation": "vertical",
        "shrink": 0.3,
    },
    ax=ax,
)

ax.set_title("Inscritos por município no ENEM - BA, 2021")
ax.axis("off")
# %%
