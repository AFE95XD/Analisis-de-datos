import pandas as pd
import numpy as np

# Cargar datos de todas las empresas
empresas = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/Latitules-Longitudes-Empresas.xlsx", sheet_name="prueba")
puntosDucto = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/coordenadasDuctoAllPuntos.xlsx", sheet_name="coordenadas")

# Filtrar las filas donde la columna "Filtro" es Verdadero
data_filtrada_empresas = empresas[empresas["Filtro"] == True]
# Filtrar solo la latitud y la longitud de las empresas que ya se filtraron
filtroTodasLasEmpresas = data_filtrada_empresas[["Latitud", "Longitud"]]
print("Las empresas son: ")
filtroTodasLasEmpresas.reset_index(drop=True, inplace=True)
print(filtroTodasLasEmpresas)

# Filtrar sola la latitud y la longitud del ducto en sus diferentes puntos
print("\nLos puntos del ducto son: ")
filtroTodosLosPuntosDucto = puntosDucto[["Latitud", "Longitud"]]
print(filtroTodosLosPuntosDucto)

# asignamos columna nueva con valores NaN
empresas["Esta en rango"] = False

# Iteramos sobre las empresas
for i in range(len(filtroTodasLasEmpresas)):
    
    # Iteramos sobre los puntos del ducto
    for j in range(len(filtroTodosLosPuntosDucto)):
        puntoLatitudMin = filtroTodosLosPuntosDucto.at[j, "Latitud"] - 0.045
        print("punto mas abajo", puntoLatitudMin)
        print(filtroTodosLosPuntosDucto.at[j, "Latitud"])
        # punto mas arriba
        puntoLatitudMax = filtroTodosLosPuntosDucto.at[j, "Latitud"] + 0.045
        print("punto mas arriba", puntoLatitudMax)
        print(filtroTodosLosPuntosDucto.at[j, "Latitud"])
        # punto mas a la izquierda
        puntoLongitudMin = filtroTodosLosPuntosDucto.at[j, "Longitud"] - 0.045
        print("punto mas a la izquierda", puntoLongitudMin)
        print(filtroTodosLosPuntosDucto.at[j, "Longitud"])
        # punto mas a la derecha
        puntoLongitudMax = filtroTodosLosPuntosDucto.at[j, "Longitud"] + 0.045
        print("punto mas a la derecha", puntoLongitudMax)
        print(filtroTodosLosPuntosDucto.at[j, "Longitud"])




        # print("----------------------------------------------------")
        # print(filtroTodasLasEmpresas.at[i, "Latitud"])
        # print("punto mas abajo", puntoLatitudMin)
        # print(filtroTodasLasEmpresas.at[i, "Latitud"] >= puntoLatitudMin)

        # print(filtroTodasLasEmpresas.at[i, "Latitud"])
        # print("punto mas arriba", puntoLatitudMax)
        # print(filtroTodasLasEmpresas.at[i, "Latitud"] <= puntoLatitudMax)

        # print(filtroTodasLasEmpresas.at[i, "Longitud"])
        # print("punto mas a la izquierda", puntoLongitudMin)
        # print(filtroTodasLasEmpresas.at[i, "Longitud"] >= puntoLongitudMin)

        # print(filtroTodasLasEmpresas.at[i, "Longitud"])
        # print("punto mas a la derecha", puntoLongitudMax)
        # print(filtroTodasLasEmpresas.at[i, "Longitud"] <= puntoLongitudMax)
        # print("----------------------------------------------------")
        # Compararo cada punto de la empresa si esta en el rango de 5 kilometros
        if puntoLatitudMin >= filtroTodasLasEmpresas.at[i, "Latitud"] and puntoLatitudMax <= filtroTodasLasEmpresas.at[i, "Latitud"] and puntoLongitudMin >= filtroTodasLasEmpresas.at[i, "Longitud"] and puntoLongitudMax <= filtroTodasLasEmpresas.at[i, "Longitud"]:
            
            # Si esta en el rango y es diferente de TRUE modifica el valor False a True
            if empresas.at[j, "Esta en rango"] == False:
                empresas.at[j, "Esta en rango"] = True

print(empresas['Esta en rango'])
# df = empresas[["Latitud", "Longitud", "Esta en rango"]]
# prueba = empresas[["Latitud", "Longitud", "Esta en rango"]]
# prueba1 = prueba[prueba["Esta en rango"] == True]

# print(prueba1)
