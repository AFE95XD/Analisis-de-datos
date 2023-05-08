import pandas as pd

archivo1 = pd.read_csv("src/bases de datos/Electricidad.csv", encoding="ISO-8859-1")
archivo2 = pd.read_csv("src/bases de datos/Manufactura.csv", encoding="ISO-8859-1")
archivo3 = pd.read_csv("src/bases de datos/Mineria.csv", encoding="ISO-8859-1")

print("--------------------")

# for col in archivo1.columns:
#     print(col)

filtroEnergia = archivo1[["ID", "Clee", "Nombre de la Unidad Económica",
                   "Razón social", "Código de la clase de actividad SCIAN", "Descripcion estrato personal ocupado", "Código Postal", "Entidad federativa", "Municipio", "Localidad", "Latitud", "Longitud"]]

filtroManufactura = archivo2[["ID", "Clee", "Nombre de la Unidad Económica",
                   "Razón social", "Código de la clase de actividad SCIAN", "Descripcion estrato personal ocupado", "Código Postal", "Entidad federativa", "Municipio", "Localidad", "Latitud", "Longitud" ]]

filtroMineria = archivo3[["ID", "Clee", "Nombre de la Unidad Económica",
                   "Razón social", "Código de la clase de actividad SCIAN", "Descripcion estrato personal ocupado", "Código Postal", "Entidad federativa", "Municipio", "Localidad", "Latitud", "Longitud"]]

# print("---------------------------------------------------------------------------------")
# print("Filtro Energia")
# print(filtroEnergia)
# print("Tiene un total de ", len(filtroEnergia), "filas")
# print("---------------------------------------------------------------------------------")
# print("Filtro Manufactura")
# print(filtroManufactura)
# print("Tiene un total de ", len(filtroManufactura), "filas")
# print("---------------------------------------------------------------------------------")
# print("Filtro Mineria")
# print(filtroMineria)
# print("Tiene un total de ", len(filtroMineria), "filas")
# print("---------------------------------------------------------------------------------")


filtroEnergia["Perteneciente"] = "Energia"
filtroManufactura["Perteneciente"] = "Manufactura"
filtroMineria["Perteneciente"] = "Mineria"

print(filtroEnergia)
print(filtroManufactura)
print(filtroMineria)

filtroEnergia.to_excel("src/bases de datos/Filtro Energia.xlsx", index=None)
filtroManufactura.to_excel("src/bases de datos/Filtro Manufactura.xlsx", index=None)
filtroMineria.to_excel("src/bases de datos/Filtro Mineria.xlsx", index=None)

# print("--------------------------------agregando----------------------------------------")
# for x in range(len(filtroEnergia)):
#     filtroEnergia["Perteneciente"] = "Energia"

# print("--------------------------------agregando----------------------------------------")
# for x in range(len(filtroManufactura)):
#     filtroManufactura["Perteneciente"] = "Manufactura"

# print("--------------------------------agregando----------------------------------------")
# for x in range(len(filtroMineria)):
#     filtroMineria["Perteneciente"] = "Mineria"

# filtros1.to_excel("src/bases de datos/Filtros Energia Electrica.xlsx", index=None)
# filtros2.to_excel("src/bases de datos/Filtros Manufactura.xlsx", index=None)
# filtros3.to_excel("src/bases de datos/Filtros Mineria.xlsx", index=None)