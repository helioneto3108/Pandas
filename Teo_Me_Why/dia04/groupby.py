# %%
import pandas as pd

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# Descobrindo quantos pontos do usuário (5f8fcbe0-6014-43f8-8b83-38cf2f4887b3) tem
cond = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[cond]
df_user

# %%
df_user["Points"].sum()

# %%
# Agora fazendo a conta para todos os outro tambem
# Primeiro fazendo do jeito contraindicado
pontos = dict()
for i in df["IdCustomer"].unique():  # .unique() -> Pega so valor unico
    condicao = df["IdCustomer"] == i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
# Fazendo pelo metodo simples
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary

# %%
df_summary.reset_index()

# %%
# Para ver a quantidade de valor unico em uma coluna
df["IdCustomer"].unique().size

# %%
# Produto entre linhas e colunas, ou seja, quantidade de informacao
df.size

# %%
df_agregadao = (
    df.groupby(["IdCustomer"])
    .agg({"Points": "sum", "UUID": "count", "DtTransaction": "max"})
    .rename(
        columns={"Points": "Valor", "UUID": "Frequência", "DtTransaction": "Recência"}
    )
    .reset_index()
)
df_agregadao

# %%
# Calculando a diferença entre a data de hj e a transação
from datetime import datetime

df["DtTransaction"]
# Vemos no dtype que ele é datetime64

# %%
data_1 = df["DtTransaction"][0]
now = datetime.now()

(now - data_1)
# O Resultado que ele me da, porém quero so os dias
# %%
(now - data_1).days

# %%
# Construindo a ideia da função para recencia
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user

# %%
diff = datetime.now() - df_user["DtTransaction"].max()
diff.days


# %%
def recencia(x):
    # O x nesse caso seria a serie inteira do groupby
    diff = datetime.now() - x.max()
    return diff.days


# %%
df_agregadao_boladao = (
    df.groupby(["IdCustomer"])
    .agg({"Points": "sum", "UUID": "count", "DtTransaction": ["max", recencia]})
    .rename(
        columns={"Points": "Valor", "UUID": "Frequência", "DtTransaction": "UltimaData"}
    )
    .reset_index()
)
df_agregadao_boladao
# %%
