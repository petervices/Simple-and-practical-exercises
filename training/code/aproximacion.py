
objetivo = int(input("escoge un numero  "))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo)>= epsilon and respuesta <= objetivo:
     respuesta += paso

if abs(respuesta**2 -objetivo) >= epsilon:
    print(f"no se encontro la raiz cuadrada {objetivo}")
else:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")

