# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
data = np.random.normal(10, 0.5, 5000)
plt.hist(data)
plt.show()
# A distribuição normal possui a média moda e mediana iguais

# %%
plt.boxplot(data)

# %%
x = np.random.normal(10, 0.5, 100)
y = np.random.uniform(0, 20, 100)

# %%
fig = plt.figure()
ax = plt.axes()

ax.scatter(x, y, marker="o", color="red", label="data 1", alpha=0.5)
ax.scatter(x * 0.5, y * 0.5, marker="v", color="black", label="data 2", alpha=0.7)

ax.legend()

# %%
# dados economicos
import plotly.express as px

# %%
px.data.gapminder()

# %%
df = px.data.gapminder().query('country == "Brazil"').set_index("year")
df

# %%
plt.plot(df.index, df["gdpPercap"], color="darkgoldenrod")
plt.title("PIB per capita do Brasil ao longo dos anos")
plt.xlabel("Anos")
plt.ylabel("PIB per capita")

# %%
title = "Relação entre a expectativa de vida e a renda per capita no Brasil"

plt.figure(figsize=(12, 4))
plt.scatter(df["lifeExp"], df["gdpPercap"], cmap="virids")
plt.xlabel("Expectativa de vida")
plt.ylabel("Renda per capita")
plt.title(title, loc="left")
plt.show()

# %%
plt.bar(x=df.index, height=df["pop"], color="red")
plt.title("População brasileira")


# %%
def filtrar_continente(continente):
    df = px.data.gapminder()
    df = df[df["continent"] == continente]
    return df


def filtrar_pais(pais, variavel):
    """Filtrar algum pais da amostra para as variaveis 'pop', 'gdpPercap' e 'lifeExp'

    Args:
        pais (str): pais que quer filtrar
        variavel (str): variavel que quer visualizar

    Returns:
        DataFrame: O DataFrame com o pais solicitado e com a variavel solicitada
    """
    df = px.data.gapminder()
    df = df[df["country"] == pais][variavel]
    return df


# %%
americas = filtrar_continente("Americas")
paises = americas["country"].unique()
plt.figure(figsize=(12, 8))

for pais in paises:
    plt.scatter(filtrar_pais(pais, "lifeExp"), filtrar_pais(pais, "gdpPercap"))

plt.legend(labels=paises, loc="best")
plt.title("Relação entre renda per capita e expectativa de vida", loc="left")
plt.xlabel("Expectativa de vida")
plt.ylabel("Renda per capita")

# %%
df[df["country"] == "Brazil"]["lifeExp"]
# %%
filtrar_pais("Brazil", "lifeExp")
# %%
df_teste = px.data.gapminder()
df_teste.iloc[168]
# %%
df_teste[df_teste["country"] == "Brazil"]["lifeExp"]
# %%
df
