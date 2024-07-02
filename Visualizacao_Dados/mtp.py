# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Setando a aleatóridade para obter mesmos resultados
np.random.seed(7)
# Pegando 10 numeros aleatorios entre 1 e 1500
y = np.random.randint(low=1, high=1500, size=10)
y

# %%
plt.plot(y)

# %%
# Insere a primeira linha no plot
plt.plot(
    y,
    color="greenyellow",
    marker="o",  # Marcador
    ms=5,  # tamanho do Marcador
    mec="blue",
    markerfacecolor="white",
    ls="-.",
)

# Inserindo a segunda linha
plt.plot(y * 2, color="rebeccapurple", marker="X", ms=5)

# Rotulos do gráfico
plt.xlabel("Eixo X", color="red", size=12)
plt.ylabel("Eixo Y")
plt.title("Titulo aqui fera", loc="left")  # loc é a posição do titulo

# Gridlines
plt.grid(axis="y", linewidth=2, alpha=0.3, linestyle="--")

# mostrar o gráfico
plt.show()

# %%
# criando os numeros para esse exemplo
np.random.seed(6)
x = np.arange(1, 11)  # Cria uma lista de 1 até o 10
y1 = np.random.randint(1, 400, 10)
y2 = np.random.randint(150, 500, 10)
y3 = np.random.randint(200, 600, 10)

# Começo figura
plt.figure(figsize=(15, 5))  # Setando o tamanho da figura
plt.suptitle("Figurona", fontsize=15)

# Criando os subplots
plt.subplot(1, 3, 1)  # O ultimo número é onde irá inserir o gráfico abaixo
plt.plot(y1, color="k")
plt.title("Subplot 1", pad=10)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.subplot(1, 3, 2)
plt.plot(x, y2, color="r")
plt.title("Subplot 2")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.subplot(1, 3, 3)
plt.plot(x, y3, color="g")
plt.title("Subplot 3")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Arrumando gráfico
plt.tight_layout(pad=4)
plt.show()

# %%
# Outro jeito para fazer o mesmo gráfico
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Figurona")

ax[0].plot(x, y1, color="k")
ax[1].plot(x, y2, color="r")
ax[2].plot(x, y3, color="g")

for i in range(3):
    ax[i].set(title=f"Subplot {i+1}", xlabel="Eixo X", ylabel="Eixo Y")
