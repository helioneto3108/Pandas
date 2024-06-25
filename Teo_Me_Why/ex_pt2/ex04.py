# Carregue os dados do arquivo data/ipea/homicidios-mulheres-negras.csv de forma correta e informe:
# Quais colunas são do tipo numérico?
# Quantas colunas são do tipo ‘object’?
# Qual o tamanho destes dados em memória?

# %%
import pandas as pd

# %%
df = pd.read_csv("../data/ipea/homicidios-mulheres-negras.csv", sep=";")
df

# %%
df.info(memory_usage="deep")
