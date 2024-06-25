# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_excel("../data/transacao_cartao.xlsx")
df

# %%
df["dtTransaction"] = pd.to_datetime(df["dtTransaction"], format="%d/%m/%Y")
df

# %%
df["Valor_Parcela"] = df["Valor"] / df["Parcelas"]
df

# %%
# Jeito melhor de fazer
df["Valor_Parcela"] = df.apply(
    lambda row: [row["Valor"] / row["Parcelas"] for i in range(row["Parcelas"])], axis=1
)
df

# %%
df_fatura = df.explode("Valor_Parcela")
df_fatura

# %%
df_fatura = df_fatura.drop(["Valor", "Parcelas"], axis=1)
df_fatura

# %%
df_fatura.groupby("idTransaction")["dtTransaction"].rank("first")

# %%
df_fatura["Months_add"] = (
    df_fatura.groupby("idTransaction")["dtTransaction"].rank("first").astype(int)
)
df_fatura


# %%
def add_months(row):
    new_date = row["dtTransaction"] + np.timedelta64(row["Months_add"], "m")
    dt_str = new_date.strftime("%Y-%m")
    return dt_str


# %%
df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura

# %%
df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura

# %%

df_fatura_mes = (
    df_fatura.groupby(["idCliente", "DtFatura"])["Valor_Parcela"].sum().reset_index()
)
df_fatura_mes
# %%
df_fatura_mes = (
    df_fatura_mes.pivot_table(
        columns="DtFatura", index="idCliente", values="Valor_Parcela"
    )
    .fillna(0)
    .reset_index()
)

# %%
df_fatura_mes.to_excel("Fatura_detalhada.xlsx")
