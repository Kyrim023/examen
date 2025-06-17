# ...................................................Variables numéricas
a = 10
b = 3

suma = a + b  # 13
resta = a - b  # 7
multiplicacion = a * b  # 30
division = a / b  # 3.333...
division_entera = a // b  # 3
modulo = a % b  # 1
potencia = a ** b  # 1000

print("OPERACIONES BÁSICAS")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("División entera:", division_entera)
print("Módulo:", modulo)
print("Potencia:", potencia)
print()

# .............................................Operaciones de comparación
x = 5
y = 10

igual = x == y
diferente = x != y
mayor = x > y
menor = x < y

print("OPERACIONES DE COMPARACIÓN")
print("¿x == y?:", igual)
print("¿x != y?:", diferente)
print("¿x > y?:", mayor)
print("¿x < y?:", menor)
print()

# .............................................Operaciones lógicas
a_bool = True
b_bool = False

and_logico = a_bool and b_bool
or_logico = a_bool or b_bool
not_logico = not a_bool

print("OPERACIONES LÓGICAS")
print("a AND b:", and_logico)
print("a OR b:", or_logico)
print("NOT a:", not_logico)
print()

# .....................................Funciones para Strings
texto = "Hola, Python"

mayusculas = texto.upper()
minusculas = texto.lower()
longitud_texto = len(texto)
reemplazo = texto.replace("Python", "Mundo")

print("FUNCIONES PARA STRINGS")
print("Texto en mayúsculas:", mayusculas)
print("Texto en minúsculas:", minusculas)
print("Longitud del texto:", longitud_texto)
print("Reemplazo de texto:", reemplazo)
print()

# Funciones para Listas
lista = [1, 2, 3]
lista.append(4)
lista.remove(2)
longitud_lista = len(lista)
lista.sort()

print("FUNCIONES PARA LISTAS")
print("Lista final:", lista)
print("Longitud de la lista:", longitud_lista)
print()

#..................................Funciones para Diccionarios
diccionario = {
    "nombre": "Ana",
    "edad": 25
}
claves = diccionario.keys()
valores = diccionario.values()
diccionario["ciudad"] = "Bogotá"
del diccionario["edad"]

print("FUNCIONES PARA DICCIONARIOS")
print("Diccionario final:", diccionario)
print("Claves:", list(claves))
print("Valores:", list(valores))
print()

#................................... Conversión de Tipos
numero = 10
texto_numero = str(numero)
lista_texto = list("Hola")
numero_flotante = float("3.14")

print("CONVERSIÓN DE TIPOS")
print("Número a texto:", texto_numero)
print("Texto a lista:", lista_texto)
print("Texto a número flotante:", numero_flotante)
