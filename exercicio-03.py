#!/usr/bin/python
# -*- coding: utf-8 -*-

# Exemplo para a resolução:
# https://benalexkeen.com/bar-charts-in-matplotlib/


# ===========================================================================
# Dados

grupo = ("0-4 ", "5-9 ", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+")

# grupo = ["0 a 4 anos", "5 a 9 anos", "10 a 14 anos", "15 a 19 anos", "20 a 24 anos", "25 a 29 anos", "30 a 34 anos", "35 a 39 anos", "40 a 44 anos", "45 a 49 anos", "50 a 54 anos", "55 a 59 anos", "60 a 64 anos", "65 a 69 anos", "70 a 74 anos", "75 a 79 anos", "80 a 84 anos", "85 a 89 anos", "90 a 94 anos", "95 a 99 anos", "100 anos e mais"]

masculino = (7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247)

feminino = (6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877, 3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989)

# ===========================================================================
# Plot

import numpy as np
import matplotlib.pyplot as plt

# Inicializa as posições em X
x_pos = np.arange(21) 

# Cria a figura com uma certa resolução
plt.figure(figsize=(12,8))

# Transforma os dados em array numpy
masculino_array = np.array(masculino)

# Adiciona a barra
plt.barh(x_pos, masculino_array, label='Masculino', color='darkgreen')

# Labels do gráfico
plt.title("População por sexo e grupo de idade")
plt.xlabel("Idades")
plt.ylabel("População")

# Marcadores das escalas
plt.yticks(x_pos, grupo, rotation=0)
plt.xticks([0,1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000],["0","1 MI","2 MI","3 MI","4 MI","5 MI","6 MI","7 MI","8 MI","9 MI"])

# Adiciona o grid
plt.grid(b=True, color='gray', linestyle='--', linewidth=0.3);

# Adiciona a legenda
plt.legend(loc='best')

# Mostra na interface e salva na pasta
print("Salvando...")
plt.savefig('./exercicio-03_barras_horizontais.png', dpi=300, bbox_inches='tight')
plt.show()
print("Salvo")