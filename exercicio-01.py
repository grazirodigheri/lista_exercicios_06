#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

# ===========================================================================
# Dados
s1 = np.array([168,398,451,337,186,232,262,349,189,204,220,220,207,239,259,258,242,331,251,323,106,1055,170])
s2 = np.array([168,400,451,300,186,200,262,349,189,204,220,220,207,239,259,258,242,331,251,180,106,1055,200])

# ===========================================================================
# Processamento

# Distância Euclidiana
dist = np.linalg.norm(s1 - s2)
print("Distância Euclidiana:", dist)

# Série Temporal com os valores médios
mean_array = np.mean([s1,s2], axis=0)
print(mean_array)

# Série Temporal com os valores máximos
max_array = np.maximum(s1,s2)
print(max_array)

# Série Temporal com os valores mínimos
min_array = np.minimum(s1,s2)
print(min_array)