# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
# Cria a figura
plt.figure(figsize=(7, 7))
# Cria o plot
plt.plot(
    [15, 20, 99],
    [13, 90, 10],
    color="lime",
    linewidth=3,  # Grossura da linha
    linestyle="--",  # Tipo da linha (olhar mais na documentação)
)
# Adicionando mais uma linha
plt.plot([99, 56, 1], [45, 23, 99], color="aqua", linewidth=2)
# Labels -> rotulos
# Rotulo do eixo x
plt.xlabel("Eixo X")
# Rotulo do eixo y
plt.ylabel("Eixo Y")
# Titulo
plt.title("Minha figura")
# Grid line
plt.grid(alpha=0.3)  # alpha é a opacidade da linha do grid

# %%
# criando subplots
fig, ax = plt.subplots(3, 2, figsize=(8, 8))

# %%
fig, ax = plt.subplots(2, 2, figsize=(8, 8))
# Adicionando linhas nas primeira caixa
ax[0, 0].plot([1, 2, 3], [5, 5, 9], color="crimson")
ax[0, 0].set(xlabel="Eixo X", ylabel="Eixo Y")
# Adicionando linhas nas segunda caixa
ax[0, 1].plot([3, 2, 1], [7, 9, 2], color="magenta")
ax[0, 1].set_title("Exemplo")
# Adicionando linhas nas terceira caixa
ax[1, 0].plot([5, 5, 9], [1, 2, 3], color="slateblue")
# Adicionando linhas nas primeira caixa
ax[1, 1].plot([4, 2, 9], [8, 1, 9], color="deeppink")
# Adicionando grid line
plt.grid(alpha=0.3)
# Separando as caixinhas
plt.tight_layout(pad=3)
# %%
