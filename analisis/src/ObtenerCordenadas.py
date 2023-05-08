# import os
# from pykml import parser
# from geopy.distance import geodesic
# from fastkml import kml

# empresas_kml = 0
# # Leer archivos KML
# with open("analisis/src/Archivos KML/Latitules-Longitudes-Empresas.kml", "r", encoding="utf-8") as file:
#     empresas_kml = parser.parse(file).getroot().Document

# ducto_kml = 0
# with open("analisis/src/Archivos KML/doc.kml", "r", encoding="utf-8") as file:
#     ducto_kml = parser.parse(file).getroot().Document


# def find_placemarks(element):
#     placemarks = []
#     if hasattr(element, "Placemark"):
#         placemarks.extend(element.Placemark)
#     for child in element.getchildren():
#         placemarks.extend(find_placemarks(child))
#     return placemarks


# empresas = find_placemarks(empresas_kml)
# ductos = find_placemarks(ducto_kml)


# def extract_line_string_coordinates(element):
#     coordinates = []
#     if hasattr(element, "LineString"):
#         for line_string in element.LineString:
#             coords_text = line_string.coordinates.text.strip().split()
#             for coord_pair in coords_text:
#                 # Asegúrate de que lon y lat estén en el orden correcto
#                 lon, lat, _ = map(float, coord_pair.split(','))
#                 coordinates.append((lat, lon))
#     for child in element.getchildren():
#         coordinates.extend(extract_line_string_coordinates(child))
#     return coordinates

# ducto_coords_list = extract_line_string_coordinates(ducto_kml)


# # Calcular distancias y filtrar empresas
# empresas_cercanas = []

# for empresa in empresas:
#     empresa_coords = tuple(
#         map(float, empresa.Point.coordinates.text.split(",")))
#         # Asegúrate de que lat y lon estén en el orden correcto
#     lat, lon = empresa_coords[1], empresa_coords[0]
#     empresa_coords = (lat, lon)

#     for ducto_coords in ducto_coords_list:
#         distancia = geodesic(empresa_coords, ducto_coords).kilometers
#         if distancia <= 5:
#             empresas_cercanas.append(empresa)
#             break


# # Crear nuevo archivo KML con ducto y empresas filtradas
# k = kml.KML()
# doc = kml.Document("1", "Empresas cercanas al ducto", "", "")
# k.append(doc)

# doc.append(ducto_kml.Placemark)

# for empresa in empresas_cercanas:
#     doc.append(empresa)

# # Guardar nuevo archivo KML
# with open("empresas_cercanas.kml", "w") as file:
#     file.write(k.to_string(prettyprint=True))

#--------------------------------------------------------------------------------------------------

# from fastkml import kml
# import pandas as pd


# def extract_coordinates_from_kml(file_path):
#     with open(file_path, "rb") as kml_file:
#         kml_content = kml_file.read().decode('utf-8')

#     k = kml.KML()
#     k.from_string(kml_content)
#     coordinates = []

#     for feature in k.features():
#         for placemark in feature.features():
#             if hasattr(placemark, "geometry"):
#                 coords = placemark.geometry.coords
#                 for coord in coords:
#                     coordinates.append(coord)
#     return coordinates

# def find_extreme_coordinates(coordinates):
#     leftmost = min(coordinates, key=lambda x: x[0])
#     rightmost = max(coordinates, key=lambda x: x[0])
#     bottommost = min(coordinates, key=lambda x: x[1])
#     topmost = max(coordinates, key=lambda x: x[1])

#     return {"leftmost": leftmost, "rightmost": rightmost, "bottommost": bottommost, "topmost": topmost}


# def export_to_csv(extreme_coordinates, file_path):
#     df = pd.DataFrame(extreme_coordinates)
#     df.to_csv(file_path, index=False)


# def export_to_excel(extreme_coordinates, file_path):
#     df = pd.DataFrame(extreme_coordinates)
#     df.to_excel(file_path, index=False)


# kml_file_path = "analisis/src/Archivos KML/doc.kml"
# coordinates = extract_coordinates_from_kml(kml_file_path)
# extreme_coordinates = find_extreme_coordinates(coordinates)

# csv_file_path = "coodenadas ducto.csv"
# export_to_csv(extreme_coordinates, csv_file_path)

# excel_file_path = "coordenadas ducto.xlsx"
# export_to_excel(extreme_coordinates, excel_file_path)

#--------------------------------------------------------------------------------------------------

# import fastkml
# import pandas as pd

# ruta_archivo_kml = "analisis/src/Archivos KML/doc.kml"

# # Lee el contenido del archivo KML en modo binario
# with open(ruta_archivo_kml, 'rb') as f:
#     contenido_binario = f.read()

# # Decodifica el contenido binario en una cadena UTF-8
# contenido_kml = contenido_binario.decode('utf-8')

# # Elimina la declaración de codificación del contenido del archivo KML
# contenido_kml = contenido_kml.replace(
#     '<?xml version="1.0" encoding="UTF-8"?>', '')

# # Crea un objeto KML
# kml = fastkml.kml.KML()

# # Carga el contenido del archivo KML
# kml.from_string(contenido_kml)

# # Obtiene todas las coordenadas de los puntos en el archivo KML
# coordenadas = []
# for feature in kml.features():
#     if isinstance(feature, fastkml.kml.Placemark):
#         if isinstance(feature.geometry, fastkml.geometry.Point):
#             coordenadas.append(
#                 (feature.geometry.coordinates[0], feature.geometry.coordinates[1]))

# # Calcula la latitud y longitud más a la izquierda, más a la derecha, más arriba y más abajo
# izquierda = min(coordenadas, key=lambda x: x[0])
# latitud_izquierda = izquierda[0]
# longitud_izquierda = izquierda[1]

# derecha = max(coordenadas, key=lambda x: x[0])
# latitud_derecha = derecha[0]
# longitud_derecha = derecha[1]

# arriba = max(coordenadas, key=lambda x: x[1])
# latitud_arriba = arriba[0]
# longitud_arriba = arriba[1]

# abajo = min(coordenadas, key=lambda x: x[1])
# latitud_abajo = abajo[0]
# longitud_abajo = abajo[1]

# # Crea un DataFrame
# df = pd.DataFrame({
#     'Latitud más a la izquierda': [latitud_izquierda],
#     'Longitud más a la izquierda': [longitud_izquierda],
#     'Latitud más a la derecha': [latitud_derecha],
#     'Longitud más a la derecha': [longitud_derecha],
#     'Latitud más arriba': [latitud_arriba],
#     'Longitud más arriba': [longitud_arriba],
#     'Latitud más abajo': [latitud_abajo],
#     'Longitud más abajo': [longitud_abajo]
# })

# # Exporta a CSV
# df.to_csv('resultado.csv', index=False)

# # Exporta a Excel
# df.to_excel('resultado.xlsx', index=False)


# import fastkml
# import pandas as pd

# ruta_archivo_kml = "analisis/src/Archivos KML/doc.kml"

# # Lee el contenido del archivo KML en modo binario
# with open(ruta_archivo_kml, 'rb') as f:
#     contenido_binario = f.read()

# # Decodifica el contenido binario en una cadena UTF-8
# contenido_kml = contenido_binario.decode('utf-8')

# # Elimina la declaración de codificación del contenido del archivo KML
# contenido_kml = contenido_kml.replace(
#     '<?xml version="1.0" encoding="UTF-8"?>', '')

# # Crea un objeto KML
# kml = fastkml.kml.KML()

# # Carga el contenido del archivo KML
# kml.from_string(contenido_kml)

# # Obtiene todas las coordenadas de los puntos en el archivo KML
# coordenadas = []
# for feature in kml.features():
#     if isinstance(feature, fastkml.kml.Placemark):
#         if isinstance(feature.geometry, fastkml.geometry.Point):
#             coordenadas.append(
#                 (feature.geometry.coordinates[0], feature.geometry.coordinates[1]))

# # Verifica si se encontraron coordenadas
# if not coordenadas:
#     print("No se encontraron puntos en el archivo KML.")
#     exit()

# # Calcula la latitud y longitud más a la izquierda, más a la derecha, más arriba y más abajo
# izquierda = min(coordenadas, key=lambda x: x[0])
# latitud_izquierda = izquierda[0]
# longitud_izquierda = izquierda[1]

# derecha = max(coordenadas, key=lambda x: x[0])
# latitud_derecha = derecha[0]
# longitud_derecha = derecha[1]

# arriba = max(coordenadas, key=lambda x: x[1])
# latitud_arriba = arriba[0]
# longitud_arriba = arriba[1]

# abajo = min(coordenadas, key=lambda x: x[1])
# latitud_abajo = abajo[0]
# longitud_abajo = abajo[1]

# # Crea un DataFrame
# df = pd.DataFrame({
#     'Latitud más a la izquierda': [latitud_izquierda],
#     'Longitud más a la izquierda': [longitud_izquierda],
#     'Latitud más a la derecha': [latitud_derecha],
#     'Longitud más a la derecha': [longitud_derecha],
#     'Latitud más arriba': [latitud_arriba],
#     'Longitud más arriba': [longitud_arriba],
#     'Latitud más abajo': [latitud_abajo],
#     'Longitud más abajo': [longitud_abajo]
# })

# # Exporta a CSV
# df.to_csv('resultado.csv', index=False)

# # Exporta a Excel
# df.to_excel('resultado.xlsx', index=False)


# from pykml import parser

# # Parsea el archivo KML
# with open('analisis/src/Archivos KML/doc.kml', 'r', encoding="utf-8") as f:
#     doc = parser.parse(f).getroot()

# # Encuentra todos los puntos de coordenadas en el archivo KML
# coordinates = []

# for placemark in doc.Document.Placemark:
#     coords = str(placemark.Point.coordinates).split(',')
#     lon = float(coords[0])
#     lat = float(coords[1])
#     coordinates.append((lat, lon))

# # Calcula la latitud y longitud más a la izquierda, derecha, arriba y abajo
# leftmost = min(coordinates, key=lambda c: c[1])
# rightmost = max(coordinates, key=lambda c: c[1])
# topmost = max(coordinates, key=lambda c: c[0])
# bottommost = min(coordinates, key=lambda c: c[0])

# # Imprime los resultados
# print("Latitud y longitud más a la izquierda:", leftmost)
# print("Latitud y longitud más a la derecha:", rightmost)
# print("Latitud y longitud más arriba:", topmost)
# print("Latitud y longitud más abajo:", bottommost)


import pandas as pd

# Lee el archivo CSV
data = pd.read_csv('analisis/src/Archivos KML/coordenadasDucto.csv')

# Calcula las coordenadas más a la izquierda, más a la derecha, más arriba y más abajo
latitud_mas_izquierda = data['Latitud'].min()
latitud_mas_derecha = data['Latitud'].max()
longitud_mas_arriba = data['Longitud'].max()
longitud_mas_abajo = data['Longitud'].min()

# Imprime los resultados
print("Latitud más a la izquierda:", latitud_mas_izquierda)
print("Latitud más a la derecha:", latitud_mas_derecha)
print("Longitud más arriba:", longitud_mas_arriba)
print("Longitud más abajo:", longitud_mas_abajo)

# Crea un DataFrame con los resultados
resultados = pd.DataFrame({
    'Coordenadas': ['Más a la izquierda', 'Más a la derecha', 'Más arriba', 'Más abajo'],
    'Latitud': [latitud_mas_izquierda, latitud_mas_derecha, '', ''],
    'Longitud': ['', '', longitud_mas_arriba, longitud_mas_abajo]
})

# Exporta el DataFrame a un archivo CSV
resultados.to_csv('resultadosCordenadasDucto.csv', index=False)
