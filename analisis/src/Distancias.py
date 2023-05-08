import pandas as pd
from geopy.distance import geodesic
import simplekml

# Leer los datos de las tiendas desde el archivo Excel
tiendas_df = pd.read_excel('ArchivoUnido.xlsx')

# Extraer las columnas de latitud y longitud
latitudes_tiendas = tiendas_df['Latitud'].tolist()
longitudes_tiendas = tiendas_df['Longitud'].tolist()

# ---------------------------------------------------------------
# Ruta al archivo KMZ
ruta_archivo_kmz = '.kmz'

# Lee el archivo KMZ y extrae los datos de coordenadas
kml = simplekml.Kml()
kml.openkmz(ruta_archivo_kmz)

# Obtén los datos del gasoducto
placemark = kml.getroot().Document.Folder.Placemark[0]  # Asegúrate de ajustar el índice si hay varios elementos en el archivo KMZ
coordinates = placemark.LineString.coordinates.text.strip()

# Separa las coordenadas individuales
coordenadas_gasoducto = [coord.split(',')[:2] for coord in coordinates.split()]

# Convierte las coordenadas en números de punto flotante
coordenadas_gasoducto = [(float(lat), float(lon)) for lon, lat, _ in coordenadas_gasoducto]

# Calcular la distancia entre cada tienda y el gasoducto
distancias = []
for i in range(len(latitudes_tiendas)):
    tienda_coords = (latitudes_tiendas[i], longitudes_tiendas[i])
    distancia = min(geodesic(tienda_coords, gasoducto_coords).kilometers for gasoducto_coords in coordenadas_gasoducto)
    distancias.append(distancia)

# Agregar las distancias como una nueva columna en el DataFrame de las tiendas
tiendas_df['Distancia al gasoducto (km)'] = distancias

# Guardar los resultados en un nuevo archivo Excel
tiendas_df.to_excel('tiendas_con_distancia.xlsx', index=False)
