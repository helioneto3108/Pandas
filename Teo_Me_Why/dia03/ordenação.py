# %%
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=";")
df

# %%
# Ordenando por o DataFrame pela pontuação
df.sort_values(by="Points", inplace=True)
df
# Tenho que colocar o inplace, pois so o metodo não realiza a atribuição
# Ou seja o DataFrame não irá mudar

# %%
# Ordenando agora do maior para o menos
df.sort_values(by="Points", ascending=False, inplace=True)
df

# %%
# Boas práticas para reatribuição
df = df.sort_values(by=["Points", "Name"], ascending=[False, True]).rename(
    columns={"Name": "Nome", "Points": "Pontos"}
)
df

# %%
