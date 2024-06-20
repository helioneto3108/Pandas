# Converta a seguinte lista de dados para uma Series Pandas e obtenha:
# Média
# Desvio Padrão
# Máximo Valor

# dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
# %%
import pandas as pd
# %%
dados = [10, 20, 42, 9,
         12, 35,24, 10,
         8, 14, 21]
dados

# %%
Dados_Series = pd.Series(dados)
Dados_Series

# %%
Dados_Series.mean()

# %%
Dados_Series.std()

# %%
Dados_Series.max()
