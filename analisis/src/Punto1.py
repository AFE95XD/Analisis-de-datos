import pandas as pd
import numpy as np

# Cargar datos de todas las empresas
todosLosDatos = pd.read_excel("analisis/ArchivoCompleto.xlsx")
empresasFiltradas = pd.read_excel("analisis/filtro15km.xlsx")

columnas = todosLosDatos.columns
df = pd.DataFrame(columns=columnas)
# df.loc[0] = todosLosDatos.loc[2]

# print(todosLosDatos)
# print(todosLosDatos.at[6, "Latitud"])
# print(todosLosDatos.at[6, "Longitud"])

# print(empresasFiltradas.at[0, "Latitud"])
# print(empresasFiltradas.at[0, "Longitud"])

# print(empresasFiltradas.at[0, "Latitud"] == todosLosDatos.at[6, "Latitud"] and empresasFiltradas.at[0, "Longitud"] == todosLosDatos.at[6, "Longitud"])

z = 0
for i in range(len(empresasFiltradas)):
    for j in range(len(todosLosDatos)):
        if empresasFiltradas.at[i, "Latitud"] == todosLosDatos.at[j, "Latitud"] and empresasFiltradas.at[i, "Longitud"] == todosLosDatos.at[j, "Longitud"]:
            df.loc[z] = todosLosDatos.loc[j]
            z+=1
df.to_excel("analisis/finalDetallado.xlsx", index=None)
print(df)