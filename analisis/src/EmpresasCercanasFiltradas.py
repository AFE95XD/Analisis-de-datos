import pandas as pd
import numpy as np

# Cargar datos de todas las empresas
empresas = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/Latitules-Longitudes-Empresas.xlsx", sheet_name="prueba")
puntosDucto = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/coordenadasDuctoAllPuntos.xlsx", sheet_name="prueba")

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

# asignamos columna nueva con valores NaN
empresas["Esta en rango"] = False

# Iteramos sobre los puntos del ducto
for i in range(len(filtroTodosLosPuntosDucto)):
    # print(i)
# for i in range(10):
    # punto mas abajo
    puntoLatitudMin = filtroTodosLosPuntosDucto.at[i, "Latitud"] - 0.045
    # print("punto mas abajo", puntoLatitudMin)
    # print(filtroTodosLosPuntosDucto.at[i, "Latitud"])
    # punto mas arriba
    puntoLatitudMax = filtroTodosLosPuntosDucto.at[i, "Latitud"] + 0.045
    # print("punto mas arriba", puntoLatitudMax)
    # print(filtroTodosLosPuntosDucto.at[i, "Latitud"])
    # punto mas a la izquierda
    puntoLongitudMin = filtroTodosLosPuntosDucto.at[i, "Longitud"] - 0.045
    # print("punto mas a la izquierda", puntoLongitudMin)
    # print(filtroTodosLosPuntosDucto.at[i, "Longitud"])
    # punto mas a la derecha
    puntoLongitudMax = filtroTodosLosPuntosDucto.at[i, "Longitud"] + 0.045
    # print("punto mas a la derecha", puntoLongitudMax)
    # print(filtroTodosLosPuntosDucto.at[i, "Longitud"])

    
    print()
    # Iteramos sobre las empresas
    for j in range(len(filtroTodasLasEmpresas)):
        print("----------------------------------------------------")
        # print(filtroTodasLasEmpresas.at[j, "Latitud"])
        # print("punto mas abajo", puntoLatitudMin)
        print(filtroTodasLasEmpresas.at[j, "Latitud"] >= puntoLatitudMin)

        # print(filtroTodasLasEmpresas.at[j, "Latitud"])
        # print("punto mas arriba", puntoLatitudMax)
        print(filtroTodasLasEmpresas.at[j, "Latitud"] <= puntoLatitudMax)

        # print(filtroTodasLasEmpresas.at[j, "Longitud"])
        # print("punto mas a la izquierda", puntoLongitudMin)
        print(filtroTodasLasEmpresas.at[j, "Longitud"] >= puntoLongitudMin)

        # print(filtroTodasLasEmpresas.at[j, "Longitud"])
        # print("punto mas a la derecha", puntoLongitudMax)
        print(filtroTodasLasEmpresas.at[j, "Longitud"] <= puntoLongitudMax)
        print("----------------------------------------------------")
        # Compararo cada punto de la empresa si esta en el rango de 5 kilometros
        if puntoLatitudMin >= filtroTodasLasEmpresas.at[j, "Latitud"] and puntoLatitudMax <= filtroTodasLasEmpresas.at[j, "Latitud"] and puntoLongitudMin >= filtroTodasLasEmpresas.at[j, "Longitud"] and puntoLongitudMax <= filtroTodasLasEmpresas.at[j, "Longitud"]:
            
            # Si esta en el rango y es diferente de TRUE modifica el valor False a True
            if empresas.at[j, "Esta en rango"] == False:
                empresas.at[j, "Esta en rango"] = True

print(empresas['Esta en rango'])
# df = empresas[["Latitud", "Longitud", "Esta en rango"]]
# prueba = empresas[["Latitud", "Longitud", "Esta en rango"]]
# prueba1 = prueba[prueba["Esta en rango"] == True]

# print(prueba1)
