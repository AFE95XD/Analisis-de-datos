# import csv
# import simplekml

# # Ruta del archivo CSV
# csv_file = 'analisis/src/Archivos KML/Latitules-Longitudes-Empresas.csv'

# # Crear objeto KML
# kml = simplekml.Kml()

# # Leer el archivo CSV
# with open(csv_file, 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Obtener los valores de latitud, longitud y descripción
#         lat = float(row['Latitud'])
#         lon = float(row['Longitud'])
#         description = row['Descripcion estrato personal ocupado']

#         # Crear el placemark y asignar el estilo de color según la descripción
#         placemark = kml.newpoint(name=description, coords=[(lon, lat)])
#         if description == '0 a 5 personas':
#             placemark.style.iconstyle.color = simplekml.Color.pink
#         elif description == '11 a 30 personas':
#             placemark.style.iconstyle.color = simplekml.Color.red
#         elif description == '31 a 50 personas':
#             placemark.style.iconstyle.color = simplekml.Color.white
#         elif description == '51 a 100 personas':
#             placemark.style.iconstyle.color = simplekml.Color.orange
#         elif description == '101 a 250 personas':
#             placemark.style.iconstyle.color = simplekml.Color.green
#         elif description == '251 y más personas':
#             placemark.style.iconstyle.color = simplekml.Color.darkturquoise

# # Guardar el archivo KML
# kml_file = 'analisis/src/Archivos KML/Latitules-Longitudes-Empresas.kml'
# kml.save(kml_file)

import csv
import simplekml

# Ruta del archivo CSV
csv_file = 'analisis/src/Archivos KML/Latitules-Longitudes-Empresas.csv'

# Crear objeto KML
kml = simplekml.Kml()

# Definir diccionario de colores
# colors = {
#     '0 a 5 personas': 'ff00ffff',     # Amarillo
#     '11 a 30 personas': 'ffff0000',    # Rojo
#     '31 a 50 personas': 'ff0000ff',    # Azul
#     '51 a 100 personas': 'ffffa500',   # Naranja
#     '101 a 250 personas': 'ff008000',  # Verde
#     '251 y mas personas': 'ff800080'   # Morado
# }
colors = {
    '0 a 5 personas': 'e5ff00ff',      #Morado
    '11 a 30 personas': 'ff0000ff',    #Rojo
    '31 a 50 personas': 'ffff0000',    #Azul
    '51 a 100 personas': 'ff008000',   #Verde
    '101 a 250 personas': 'FF0099FF',  #Naranja
    '251 y mas personas': 'ff00ffff'   # Amarillo
}

# Leer el archivo CSV
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Obtener los valores de latitud, longitud y descripción
        lat = float(row['Latitud'])
        lon = float(row['Longitud'])
        description = row['Descripcion estrato personal ocupado']

        # Crear estilo de ícono personalizado con el color correspondiente
        style = simplekml.Style()
        style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png'
        style.iconstyle.color = colors[description]

        # Crear el placemark con el estilo de ícono personalizado
        placemark = kml.newpoint(name=description, coords=[(lon, lat)])
        placemark.style = style

# Guardar el archivo KML
kml_file = 'analisis/src/Archivos KML/Latitules-Longitudes-Empresas.kml'
kml.save(kml_file)
