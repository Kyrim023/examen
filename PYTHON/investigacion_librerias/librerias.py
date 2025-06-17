import pandas as pd

datos = {
    'Producto': ['Aceite', 'Filtro', 'Llantas'],
    'Precio': [12000, 8000, 150000],
    'Stock': [20, 35, 10]
}

df = pd.DataFrame(datos)

print("Tabla de productos:")
print(df)

df['Total'] = df['Precio'] * df['Stock']

print("\n Tabla con total calculado:")
print(df)

bajo_stock = df[df['Stock'] < 15]
print("\n Productos con poco stock:")
print(bajo_stock)









"""
Archivo 5: investigacion_librerias

Librería investigada: pandas


 Funcionalidad:
#...............................
La librería "pandas" se usa en Python para el análisis y manipulación de datos estructurados, como tablas o bases de datos. 
Permite trabajar con grandes volúmenes de datos, realizar filtros, agrupaciones, transformaciones y más.
Es fundamental en áreas como ciencia de datos, machine learning, análisis financiero, etc.


Sintaxis básica:
#...............................
import pandas as pd

# Crear un DataFrame desde un diccionario
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [23, 30, 27]
})

print(df)


 Aplicaciones:
#...............................
- Análisis de datos en empresas (ventas, clientes, inventarios).
- Limpieza de datos antes de entrenar modelos de Machine Learning.
- Lectura y escritura de archivos CSV, Excel, SQL.
- Estadísticas y generación de reportes automatizados.


 Ejemplo de código:
#...............................

"""

