import pandas as pd

# Cargar datos de todas las empresas
empresas = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/Latitules-Longitudes-Empresas.xlsx", sheet_name="empresasCopia")
puntosDucto = pd.read_excel("analisis/src/Archivos KML/Nueva carpeta/coordenadasDuctoAllPuntos.xlsx", sheet_name="coordenadasDuctoAllPuntos")

# Filtrar las filas donde la columna "Filtro" es Verdadero
data_filtrada_empresas = empresas[empresas["Filtro"] == True]
# Filtrar solo la latitud y la longitud de las empresas que ya se filtraron
filtroTodasLasEmpresas = data_filtrada_empresas[["Latitud", "Longitud",'Descripcion estrato personal ocupado', 'Dentro_lat_min', 'Dentro_lat_max', 'Dentro_long_min', 'Dentro_long_max', "Filtro"]]
print("\nLas empresas son: \n")
filtroTodasLasEmpresas.reset_index(drop=True, inplace=True)
print(filtroTodasLasEmpresas)

# Filtrar sola la latitud y la longitud del ducto en sus diferentes puntos
print("\nLos puntos del ducto son: \n")
filtroTodosLosPuntosDucto = puntosDucto[["Latitud", "Longitud"]]
print(filtroTodosLosPuntosDucto)

# asignamos columna nueva con valores FALSE
filtroTodasLasEmpresas["Esta en rango"] = False

kilometros = 15

# Iteramos sobre las empresas
for i in range(len(filtroTodasLasEmpresas)):
    siEsta = False
    # Iteramos sobre los puntos del ducto
    for j in range(len(filtroTodosLosPuntosDucto)):
        # Punto mas abajo
        puntoLatitudMin = filtroTodosLosPuntosDucto.at[j, "Latitud"] - (kilometros/85)
        # punto mas arriba
        puntoLatitudMax = filtroTodosLosPuntosDucto.at[j, "Latitud"] + (kilometros/85)
        # punto mas a la izquierda
        puntoLongitudMin = filtroTodosLosPuntosDucto.at[j, "Longitud"] - (kilometros/84.97)
        # punto mas a la derecha
        puntoLongitudMax = filtroTodosLosPuntosDucto.at[j, "Longitud"] + (kilometros/84.97)
        # Compararo cada punto de la empresa si esta en el rango de 5 kilometros
        if filtroTodasLasEmpresas.at[i, "Latitud"] >= puntoLatitudMin and filtroTodasLasEmpresas.at[i, "Latitud"]  <= puntoLatitudMax and filtroTodasLasEmpresas.at[i, "Longitud"]  >= puntoLongitudMin and filtroTodasLasEmpresas.at[i, "Longitud"] <= puntoLongitudMax:
            print("Entro")
            # Si esta en el rango y es diferente de FALSE modifica el valor False a True
            siEsta = True
            break
    if siEsta == True:
        print("")
        filtroTodasLasEmpresas.at[i,'Esta en rango'] = siEsta

print("\nEl resultado es:\n")
# print(empresas[['Latitud','Longitud','Descripcion estrato personal ocupado','Dentro_lat_min','Dentro_lat_max', 'Dentro_long_min', 'Dentro_long_max','Filtro', 'Esta en rango']])
print(filtroTodasLasEmpresas)
nuevoExcel = filtroTodasLasEmpresas.to_excel("analisis/src/Archivos KML/Nueva carpeta/Resultados 15 kilometros.xlsx", index=None)