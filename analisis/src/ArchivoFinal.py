import pandas as pd

archivo1 = pd.read_excel("src/Archivos Ordenados/Filtro Energia.xlsx")
archivo2 = pd.read_excel("src/Archivos Ordenados/Filtro Manufactura.xlsx")
archivo3 = pd.read_excel("src/Archivos Ordenados/Filtro Mineria.xlsx")

result = pd.concat([archivo1, archivo2, archivo3], axis=0)

result.to_excel("ArchivoUnido.xlsx", index=False)
