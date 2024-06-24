# Converta o seguinte dicionário para DataFrame e obtenha:
# Sumário de cada coluna
# Média da coluna idade
# Último nome da coluna nome

# dados = {"nome":["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}
# %%
import pandas as pd

# %%
dados = {"nome": ["Téo", "Nah", "Napoleão"], "idade": [31, 32, 14]}
dados

# %%
df = pd.DataFrame(dados)
df

# %%
sumario_numerico = df.describe()
sumario_numerico

# %%
df["nome"].describe()
# Se eu tivesse dois 'Napoleão' o top seria 'Napoleão' com freq == 2

# %%
sumario_numerico["idade"]["mean"]
# ou poderia ser df['idade'].mean()

# %%
df["nome"].iloc[-1]
# Poderia ser também df['nome'].tail(1)
