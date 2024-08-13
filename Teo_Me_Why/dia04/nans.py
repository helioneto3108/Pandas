# %%
import pandas as pd
import numpy as np

# %%
data = {
    "nome": ["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade": [31, 32, 34, 12, np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan],
}

df = pd.DataFrame(data)
df

# %%
# Para saber quantos NAs (dado faltante) eu tenho na minha serie de ref
# .isna faz a comparação logica perguntando para cada elemento da minha serie se ele é um valor nulo ou nao
# o retorno disso é uma serie com True e False. Eu posso somar pois cada True equivale a 1 e False a 0
df["idade"].isna().sum()

# %%
df.isna()

# %%
df.isna().sum()

# %%
# Ver as medias de NAs em cada coluna
df.isna().mean()

# %%
# Preenchendo os NAs com as medias
df.fillna(
    {
        "idada": df["idade"].mean(),
        "renda": df["renda"].mean(),
    }
)
# Caso queria colocar um escalar como df.fillna(0), todos os NAs serão substituidos por 0
# Essa prática da media é boa para trabalhar com analise de dados, não com machine learning
# Isso não reatribuiu vc tem que colocar o inplace ou df = df.fillna()

# %%
# Tirando todas as linhas que tem NAs
df.dropna()

# %%
# Removendo agora somente onde todas as colunas de ref da linha forem NAs
df.dropna(subset=["idade", "renda"], how="all")

# %%
# Removendo agora se as linhas do subset tiver pelo menos 1 NA
df.dropna(subset=["idade", "renda"], how="any")

# %%
# Para excluir coluna que possui NAs
df.dropna(axis=1)

# %%
# Excluido por quantidade de não NAs
df.dropna(axis=1, thresh=4)
# Ou seja, o thresh é o minino de valores não nulos para ele não excluir a coluna
# %%
df.dropna(axis=1, thresh=3)
# %%
df.dropna(axis=1, thresh=5)
# %%
