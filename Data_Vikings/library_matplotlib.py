# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
# Cria a figura
plt.figure(figsize = (7, 7))
# Cria o plot
plt.plot([15, 20, 99], [13, 90, 10],
         color = 'lime',
         linewidth = 3, # Grossura da linha
         linestyle = '--' # Tipo da linha (olhar mais na documentação)
         )
# Adicionando mais uma linha
plt.plot([99, 56, 1], [45, 23, 99],
         color = 'aqua',
         linewidth = 2)
# Labels -> rotulos
# Rotulo do eixo x 
plt.xlabel('Eixo X')
# Rotulo do eixo y 
plt.ylabel('Eixo Y')
# Titulo
plt.title('Minha figura')
# Grid line
plt.grid(alpha = 0.3) # alpha é a opacidade da linha do grid

# %%
