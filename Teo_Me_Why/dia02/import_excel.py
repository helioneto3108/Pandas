# %%
import pandas as pd

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %%
df.shape

# %%
df.head()

# %%
df.tail()

# %%
df = df[["UUID", "Points", "IdCustomer", "DtTransaction"]]
df

# %%
df.info(memory_usage="deep")

# %%
