# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("data/dados_enem_2021_BA.csv")
df

# %%
# Deixando como padrão a visualização de 100 colunas do DataFrame
pd.set_option("display.max_columns", 100)
df

# %%
# Agora para linhas, caso o numero colocado n atenda ao numero de linhas no DF ele não irá mostrar e usará o default de 10 linhas
pd.set_option("display.max_rows", 60)
df
# pd.reset_option('display.max_rows') -> Para voltar ao normal, senão voltar gasto computacional é muito grande

# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%
# Sem verificar o espaço em disco
df.info()

# %%
df.columns

# %%
# Verificando os tipos das colunas
df.dtypes

# %%
df.dtypes == "object"

# %%
# Trazendo so as colunas de objeto
df.select_dtypes(include=object)

# %%
# Trazendo so as colunas de objeto
df.select_dtypes(include=object).columns

# %%
df.isna().sum()

# %%
df.isna().sum().sort_values(ascending=False)

# %%
# Verificando agr com as porcentagens ordenando da maior para a menor
(df.isna().sum() / df.shape[0] * 100).sort_values(ascending=False)

# %%
# Outro jeito de fazer
df.isna().mean().sort_values(ascending=False)

# %%
df.describe()

# %%
df.describe().transpose()

# %%
# Outro jeito de escrever
df.describe().T[26:30]

# %%
# Fazendo os describe somente das notas
df.describe().T.iloc[list(range(26, 30)) + [37]]

# %%
# Quantidade de valores unicos
df.nunique().sort_values()

# %%
df.nunique().sort_values(ascending=False)

# %%
# Distribuição de frequencia do tipo de escola
# 1 = n responder, 2 = publica, 3 = privada
df["TP_ESCOLA"].value_counts()

# %%
# Jeitos de puxar colunas
df.loc[:, "TP_ESCOLA"]

# %%
# Outro jeito de puxar a coluna
df["TP_ESCOLA"]

# %%
df[["TP_ESCOLA", "TP_SEXO"]]

# %%
df.select_dtypes(include=int)

# %%
df.select_dtypes(include=[int, float])

# %%
df.select_dtypes(exclude=object)

# %%
# Para pegar os nomes das colunas categoricas
cat_col = df.select_dtypes(include=object).columns.tolist()
cat_col

# %%
# Filtros
# Alunos de escola publica
df.query("TP_ESCOLA == 2")

# %%
df.query("TP_ESCOLA == 2").NU_NOTA_MT.mean()

# %%
df.query("TP_ESCOLA == 2")["NU_NOTA_MT"].mean()

# %%
df.query("TP_ESCOLA == 3").NU_NOTA_MT.mean()

# %%
df.query("TP_ESCOLA == 2").NU_NOTA_MT.agg(["mean", "median"])

# %%
df.query("TP_ESCOLA == 3").NU_NOTA_MT.agg(["mean", "median"])

# %%
# Duas ou mais condições (AND)
df.query('(TP_SEXO == "M") & (IN_TREINEIRO == 1)').head()

# %%
df.query('(TP_SEXO == "M") & (IN_TREINEIRO == 1)').sample(5)

# %%
# Mesmo consulta porem sem o query
df[(df["TP_SEXO"] == "M") & (df["IN_TREINEIRO"] == 1)].head()

# %%
# Outra maneira usando loc
df.loc[(df["TP_SEXO"] == "M") & (df["IN_TREINEIRO"] == 1)].head()

# %%
# Duas ou mais condições (or)
df.query('(TP_SEXO == "M") | (IN_TREINEIRO == 1)').sample(5)

# %%
# Criando uma mascara
df.TP_SEXO == "M"

# %%
# Fazendo um filtro com essa mascara
df[df["TP_SEXO"] == "M"]

# %%
# Negação
df.NO_MUNICIPIO_PROVA.isin(["Itabuna", "Salvador"])

# %%
df[df.NO_MUNICIPIO_PROVA.isin(["Itabuna", "Salvador"])]

# %%
# Para negar essa condição é so fazer isso
df[~(df.NO_MUNICIPIO_PROVA.isin(["Itabuna", "Salvador"]))]
# Ele irá pegar quem não mora em Itabuna, Salvador

# %%
# Outra maneira de escrever a condição
df[df["NO_MUNICIPIO_PROVA"].isin(["Itabuna", "Salvador"])]

# %%
# Outra maneira de escrever a condição negando
df[~(df["NO_MUNICIPIO_PROVA"].isin(["Itabuna", "Salvador"]))]

# %%
# Visualização de dados
# Pegando as colunas de notas e tirando a parte de redação 'comp'
df.columns[df.columns.str.contains("NOTA")]

# %%
# Para entender o que está acontecendo no comando acima
df.columns.str.contains("INSCRICAO")
# Com essa linha eu crio uma mascara booleana no meu array e seu
# E se eu colocar dentro de um df.colums eu vou fazer um filtro

# %%
provas = df.columns[
    df.columns.str.contains("NOTA") & (~df.columns.str.contains("COMP"))
].tolist()
provas

# %%
id_candidato = ["NU_INSCRICAO"]
id_candidato

# %%
# Criando grafico de barras
df.TP_ESCOLA.value_counts().plot(kind="bar")
plt.title("Tipo de escola dos participantes do ENEM 2021 na Bahia")

# %%
# Melhorando o gráfico
df.TP_ESCOLA.value_counts().plot(kind="bar", color="green")
# titulo do gráfico
plt.title("Tipo de escola dos participantes do ENEM 2021 na Bahia")
# titulo do eixo x
plt.xlabel("Tipo de Escola")
# titulo do eixo y
plt.ylabel("Quantidade")

# %%
(
    df["NO_MUNICIPIO_PROVA"]
    .value_counts()
    .reset_index()
    .rename(columns={"NO_MUNICIPIO_PROVA": "Município", "count": "Quantidade"})
    .set_index("Município")
    .plot(kind="barh")
)


# %%
(
    df["NO_MUNICIPIO_PROVA"]
    .value_counts()
    .nlargest(n=15)
    .plot(
        kind="barh",
        color="red",
        legend=False,
        xlabel="Quantidade",
        ylabel="Município",
        title="Top 15 municípios baíanos com maior quantidade de inscritos no enem 2021",
    )
)

# %%
# Pegando o top 15 para o gráfico ficar legivel
(
    df["NO_MUNICIPIO_PROVA"]
    .value_counts()
    .reset_index()
    .rename(columns={"NO_MUNICIPIO_PROVA": "Município", "count": "Quantidade"})
    .nlargest(n=15, columns="Quantidade")
    .set_index("Município")
    .plot(kind="barh")
)
# Para não usar o paretense eu posso usar:
# df['NO_MUNICIPIO_PROVA']\
#    .vale_counts()\
#     .reset_index

# %%
(
    df["NO_MUNICIPIO_PROVA"]
    .value_counts()
    .reset_index()
    .rename(columns={"NO_MUNICIPIO_PROVA": "Município", "count": "Quantidade"})
    .nlargest(n=15, columns="Quantidade")
    .set_index("Município")
    .plot(
        kind="barh",
        color="red",
        legend=False,
        xlabel="Quantidade",
        title="Top 15 municípios baíanos com maior quantidade de inscritos no enem 2021",
    )
)

# %%
df.TP_ESCOLA.map({1: "Não respondeu", 2: "Públcia", 3: "Privada"})

# %%
# Outro jeito de fazer
df["TP_ESCOLA"].map({1: "Não respondeu", 2: "Pública", 3: "Privada"})

# %%
(
    df.TP_ESCOLA.map({1: "Não respondeu", 2: "Públcia", 3: "Privada"})
    .value_counts()
    .plot(kind="pie", title="Comparação dos tipos de escola")
)

# %%
(
    df.TP_ESCOLA.map({1: "Não respondeu", 2: "Públcia", 3: "Privada"})
    .value_counts()
    .plot(
        kind="pie",
        title="Comparação dos tipos de escola",
        ylabel="Quantidade",
        autopct="%.2f",
    )
)

# %%
# Gráfico de dispersão
df.plot(kind="scatter", x="NU_NOTA_MT", y="NU_NOTA_CN", color="purple")

# %%
# Histograma
df.NU_NOTA_CH.plot(kind="hist", color="pink")

# %%
# Boxplot -> Bom para ver outliers
df["NU_NOTA_MT"].plot(kind="box")

# %%
df[provas].plot(kind="box")

# %%
df.NU_NOTA_MT.plot(kind="kde", color="orange")
# Esse gráfico faz uma aproximação/estimativa da densidade de propabilidade da coluna ref

# %%
(
    df.groupby(by=["NO_MUNICIPIO_PROVA"])
    .agg({"NU_NOTA_MT": np.mean})
    .reset_index()
    .rename(columns={"NU_NOTA_MT": "Nota", "NO_MUNICIPIO_PROVA": "Município"})
    .nlargest(n=10, columns="Nota")
    .plot(
        x="Município",
        y="Nota",
        figsize=(15, 10),
        color="k",
        ylabel="Média em Matemática",
        title="Nota média em Matemática por municípios",
        # ylim    = [520, 545] -> para limitar o eixo y
    )
)

# %%
(df.groupby(by=["NO_MUNICIPIO_PROVA"]).agg({"NU_NOTA_MT": np.mean}).reset_index())

# %%
# Ordenação
# Pegando um subset com 10 amostras aleatorias
df_subset = df[id_candidato + provas].sample(10, random_state=9999)
df_subset

# %%
df_subset.sort_values(by="NU_NOTA_MT", ascending=False)

# %%
df_subset.sort_values(by="NU_NOTA_MT", ascending=False, na_position="first")

# %%
df_subset.sort_values(by="NU_NOTA_MT", ascending=False, na_position="last")

# %%
# Exercicio: pegar as 10 melhores notas de matematica de salvador
df_salvador_top10 = df.query('NO_MUNICIPIO_PROVA == "Salvador"')[id_candidato + provas]
df_salvador_top10

# %%
# Outro jeito de fazer
# Vale lembrar que quando coloco '()' e como se fosse uma linha
(
    df[df["NO_MUNICIPIO_PROVA"] == "Salvador"][
        id_candidato + provas + ["NO_MUNICIPIO_PROVA"]
    ]
)

# %%
df_salvador_top10.sort_values(by=["NU_NOTA_MT"], ascending=False)[:11]

# %%
# Fazendo a mesma coisa de um jeito mais facil
df_salvador_top10.nlargest(10, columns="NU_NOTA_MT")

# %%
# Para os 10 menores
df_salvador_top10.nsmallest(10, columns="NU_NOTA_MT")

# %%
