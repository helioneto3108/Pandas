# %%
import pandas as pd
import numpy as np
import seaborn as sns

# Definir tema da aparecina dos gráficos
sns.set_theme(style="darkgrid")
# %%
# Puxando base de dados de restaurante do proprio seaborn
dados = sns.load_dataset("tips")
dados

# %%
# renomeando as colunas
dados = dados.rename(
    columns={
        "total_bill": "Total conta",
        "tip": "Gorjeta",
        "sex": "Gênero",
        "smoker": "Fumante",
        "day": "Dia da semana",
        "time": "Refeição",
        "size": "Tamanho mesa",
    }
)
dados

# %%
# Gráfico relplot
sns.relplot(x="Total conta", y="Gorjeta", data=dados)

# %%
# Gráfico relplot, passando outro parametro como classe no gráfico
sns.relplot(x="Total conta", y="Gorjeta", data=dados, hue="Gênero")

# %%
# Gráfico de linha com 2 eixos
sns.relplot(x="Total conta", y="Gorjeta", data=dados, kind="line")

# %%
# Gráfico de linha com 2 eixos com dois parametros
sns.relplot(x="Total conta", y="Gorjeta", data=dados, kind="line", hue="Fumante")

# %%
# Histplot
sns.histplot(data=dados, x="Total conta")

# %%
sns.histplot(data=dados, x="Total conta", hue="Fumante")

# %%
# barplot
sns.barplot(data=dados, x="Gênero", y="Total conta", hue="Fumante")

# %%
sns.pairplot(dados)

# %%
sns.pairplot(dados, hue="Gênero")

# %%
# Boxplot
sns.boxplot(data=dados, x="Dia da semana", y="Total conta", palette="tab10")

# %%
sns.boxplot(
    data=dados, x="Dia da semana", y="Total conta", palette="tab10", hue="Gênero"
)

# %%
# Tentando plotar genero no grafico de barras
sns.countplot(data=dados, x="Gênero")

# %%
# Tentando plotar no grafico de barras
sns.countplot(data=dados, x="Gênero", hue="Fumante")
