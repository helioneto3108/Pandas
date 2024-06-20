# %%
import pandas as pd
# %%
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

# %%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
# Mudar o tipo de object para int caso precise
#df_customers['Points'].astype(int)

df_customers.describe()

# %%
# Somando mais 1000 (no pontos) para todos as linhas
# df_customers['Points'] + 1000
# Posso fazer isso com todas as operações em colunas númericas

condicao = df_customers['Points'] > 1000
condicao
# %%
# So me retornara valores True
df_customers[condicao]
# É desse jeito que se faz filtros em pandas

# %%
# Descobrindo quem é o maior pontuador
maximo = df_customers['Points'].max() # Descobre qual a maior pontuação
condicao_2 = df_customers['Points'] == maximo # Faz a comparação vetorial, ou seja, com todos os valores e ve se e True or False
df_customers[condicao_2] # Mostra o resultado

# %%
# Forma mais curta de fazer
condicao_2 = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao_2]

# %%
# Froma mais curta ainda e mais utilizada
df_customers[df_customers['Points'] == df_customers['Points'].max()]
# Ou seja o [] de um dataframe pode ser utilizado como filtro
# df_customers['Points'].max() -> é considerado o escalar da operações
# O processo acima mostra a base de como é feito esse filtro

# %%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name']

# %%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]
# Isso é chamado de condições logicas -> filtro

# %%
