# %%
import pandas as pd

# %%
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %%
df_customers.shape

# %%
df_customers.info(memory_usage="deep")

# %%
# Mudar o tipo de object para int caso precise
# df_customers['Points'].astype(int)

df_customers.describe()

# %%
# Somando mais 1000 (no pontos) para todos as linhas
# df_customers['Points'] + 1000
# Posso fazer isso com todas as operações em colunas númericas

condicao = df_customers["Points"] > 1000
condicao
# %%
# So me retornara valores True
df_customers[condicao]
# É desse jeito que se faz filtros em pandas

# %%
# Descobrindo quem é o maior pontuador
maximo = df_customers["Points"].max()  # Descobre qual a maior pontuação
condicao_2 = (
    df_customers["Points"] == maximo
)  # Faz a comparação vetorial, ou seja, com todos os valores e ve se e True or False
df_customers[condicao_2]  # Mostra o resultado

# %%
# Forma mais curta de fazer
condicao_2 = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao_2]

# %%
# Froma mais curta ainda e mais utilizada
df_customers[df_customers["Points"] == df_customers["Points"].max()]
# Ou seja o [] de um dataframe pode ser utilizado como filtro
# df_customers['Points'].max() -> é considerado o escalar da operações
# O processo acima mostra a base de como é feito esse filtro

# %%
df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"]

# %%
df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"].iloc[0]
# Isso é chamado de condições logicas -> filtro

# %%
# Filtro colocando duas condicões
condicao_Dupla = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_customers[condicao_Dupla]

# %%
df_customers[condicao_Dupla].describe()

# %%
# Os dataframes se comportam como lista na questão de linkagem
# Ou seja caso coloque um filtro e atribua ele em uma variavel ele terá um link entre os 2 dataframes
# Ou seja caso eu altere 1 irá alterar no outro
# Para resolver esse problema deve-se usar o comando metodo .copy, que irá duplicar o DF ao inves de fazer a linkagem
df_1000_2000 = df_customers[condicao_Dupla].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
# Desse jeito ao alterar a planilha não alterará a minha planilha original. Como acontece em listas

# %%
# Para navegar entre duas colunas
df_customers[["UUID", "Name"]]

# %%
# jogando os nomes de uma coluna para uma lista pelo metodo .tolist
colunas = df_customers.columns.tolist()
# Poderia ter feito colunas = list(df_customers.columns)
colunas

# %%
# Ordenando as ordens da coluna em ordem alfabetica
colunas.sort()
colunas

# %%
df_customers = df_customers[colunas]
df_customers

# %%
# renomeando o nome das colunas
df_customers = df_customers.rename(columns={"Name": "Nome", "Points": "Pontos"})
df_customers

# %%
# Outro jeito, que já aplica a renomeação no dataframe, sem precisar de reatribuição
df_customers.rename(columns={"UUID": "Id"}, inplace=True)
df_customers

# %%
