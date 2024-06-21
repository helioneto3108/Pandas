# %%
import pandas as pd

# %%
# Parquet é utilizado pela otimização, os arquivos são mais leves e com uma leitura mais rápida
df = pd.read_parquet("../data/transactions_cart.parquet")
df

# %%
df.info(memory_usage=True)
# %%
