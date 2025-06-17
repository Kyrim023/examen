# .........................................................Ciclo FOR
print("CICLO FOR")
frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print("Me gusta la", fruta)
print()




# .....................................................Ciclo WHILE
print("CICLO WHILE")
contador = 0
while contador < 3:
    print("Contando:", contador)
    contador += 1
print()





# ...........................................Condicionales
print("CONDICIONALES")
edad = 20
if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres adulto mayor.")
print()




# ........................................break y continue
print("break y continue")
for numero in range(1, 6):
    if numero == 3:
        print("Saltando el 3 ")
        continue
    if numero == 5:
        print("Se encontró el 5")
        break
    print("Número:", numero)
print()




# ..........................................else en bucles
print("else")
for n in range(3):
    print("Iteración:", n)
else:
    print("El ciclo terminó normalmente sin break.")
