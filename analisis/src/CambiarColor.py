import csv
import simplekml

# Leer el archivo CSV
archivo_csv = 'analisis/src/Archivos KML/Latitules-Longitudes-Empresas.csv'

# Crear un objeto KML
kml = simplekml.Kml()

# Definir los colores para cada categoría
colores = {
    '0 a 5 personas': 'ffff00',  # Amarillo
    '11 a 30 personas': 'ff0000',  # Rojo
    '31 a 50 personas': '0000ff',  # Azul
    '51 a 100 personas': 'ff7f00',  # Naranja
    '101 a 250 personas': '00ff00',  # Verde
    '251 y mas personas': 'a020f0'   # Morado
}

# Leer el archivo CSV y agregar puntos KML con colores
with open(archivo_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Saltar la fila de encabezado
    for row in reader:
        lat, lon, descripcion = row
        punto = kml.newpoint(coords=[(float(lon), float(lat))])
        punto.style.iconstyle.color = simplekml.Color.hex(colores[descripcion])

# Guardar el archivo KML
kml.save('result.kml')
