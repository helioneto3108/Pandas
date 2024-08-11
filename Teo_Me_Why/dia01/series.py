# %%
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades

# %%
# Fazendo os caluclos no seco de algumas estatisticas

media = sum(idades) / len(idades)
media

# %%
total = 0
for i in idades:
    total += (media - i) ** 2

variancia = total / (len(idades) - 1)
variancia

# %%
# Transformando a lista em serie

series_idades = pd.Series(idades)
series_idades

# %%
series_idades.mean()

# %%
series_idades.var()

# %%
series_idades.median()

# %%
series_idades.quantile(0.75)

# %%
series_idades.describe()

# %%
# verificando atráves de um atributo (caracterisitcas), quantas linhas minha serie tem
series_idades.shape

# %%
idades[0]

# %%
series_idades[0]
# Não posso usar series_idades[-1]

# %%
series_idades.index = ["t", "e", "o", "c"]
series_idades

# %%
series_idades["t"]

# %%
series_idades[0]
# Ele ainda encontra, pois caso ele não encontre pelo indice ele ira procurar por posição caso vc coloque um numero

# %%
# Comando para procurar atraves da posição e não pelo indice
series_idades.iloc[0:2]

# %%
# Comando para procurar atraves do indice
series_idades.loc["t":"e"]

# %%
series_idades.name = "idades"
series_idades
# Tem como atribuit series_idades = pd.Series(idades, name = 'idade')

# %%
