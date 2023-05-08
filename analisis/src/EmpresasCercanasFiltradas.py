import pandas as pd
import numpy as np

# Cargar datos de todas las empresas
empresas = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/Latitules-Longitudes-Empresas.xlsx", sheet_name="Copia de Copia de Hoja 1")
puntosDucto = pd.read_csv("analisis/src/Archivos KML/coordenadasDuctoAllPuntos.csv")
print("-----------------------------------------------------------------------------------------")
prueba = empresas[["Latitud", "Longitud", "Filtro"]]
prueba1 = prueba[prueba["Filtro"] == False]
print(prueba1)
print("-----------------------------------------------------------------------------------------")
# Filtrar las filas donde la columna "Filtro" es Verdadero
data_filtrada_empresas = empresas[empresas["Filtro"] == True]
# Filtrar solo la latitud y la longitud de las empresas que ya se filtraron
filtroTodasLasEmpresas = data_filtrada_empresas[["Latitud", "Longitud"]]
print("Las empresas son: ")
filtroTodasLasEmpresas.reset_index(drop=True, inplace=True)
print(filtroTodasLasEmpresas)
# print(filtroTodasLasEmpresas.head(10))
print("#######################################################################")
# Filtrar sola la latitud y la longitud del ducto en sus diferentes puntos
print("Los puntos del ducto son: ")
filtroTodosLosPuntosDucto = puntosDucto[["Latitud", "Longitud"]]
print(filtroTodosLosPuntosDucto)

# Iteramos sobre los puntos del ducto
for i in range(len(filtroTodosLosPuntosDucto) - 1):
    print(i)
# for i in range(2):
    # punto mas abajo
    puntoLatitudMin = filtroTodosLosPuntosDucto.at[i, "Latitud"] - 0.045
    # punto mas arriba
    puntoLatitudMax = filtroTodosLosPuntosDucto.at[i, "Latitud"] + 0.045
    # punto mas a la derecha
    puntoLongitudMin = filtroTodosLosPuntosDucto.at[i, "Longitud"] + 0.045
    # punto mas a la izquierda
    puntoLongitudMax = filtroTodosLosPuntosDucto.at[i, "Longitud"] - 0.045

    # asignamos columna nueva con valores NaN
    empresas["Esta en rango"] = False

    # Iteramos sobre las empresas
    for j in range(len(filtroTodasLasEmpresas)-1):
        # Compararo cada punto de la empresa si esta en el rango de 5 kilometros
        if puntoLatitudMin > filtroTodasLasEmpresas.at[j, "Latitud"] and puntoLatitudMax < filtroTodasLasEmpresas.at[j, "Latitud"] and puntoLongitudMin > filtroTodasLasEmpresas.at[j, "Longitud"] and puntoLongitudMax < filtroTodasLasEmpresas.at[j, "Longitud"]:
            # Si esta en el rango y es diferente de TRUE modifica el valor False a True
            if empresas.at[j, "Esta en rango"] != True:
                empresas.at[j, "Esta en rango"] = True

prueba = empresas[["Latitud", "Longitud", "Esta en rango"]]
prueba1 = prueba[prueba["Esta en rango"] == True]

print(prueba1)
