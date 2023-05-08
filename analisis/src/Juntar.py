import simplekml
import zipfile
import os

def agregar_kml_a_kmz(ruta_kmz, ruta_kml):
    # Extraer el archivo KML del KMZ
    with zipfile.ZipFile(ruta_kmz, 'r') as kmz:
        kmz.extractall()

    # Leer el archivo KML
    kml = simplekml.Kml()
    kml.open(ruta_kml)

    # Agregar el contenido del KML al KMZ
    with zipfile.ZipFile(ruta_kmz, 'a') as kmz:
        kmz.write(ruta_kml, os.path.basename(ruta_kml))

    # Eliminar el archivo KML
    os.remove(ruta_kml)


# Rutas de los archivos KMZ y KML
ruta_kmz = 'ruta/al/archivo.kmz'
ruta_kml = 'ruta/al/archivo.kml'

# Agregar el archivo KML al KMZ
agregar_kml_a_kmz(ruta_kmz, ruta_kml)
