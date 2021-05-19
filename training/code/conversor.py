menu = """
Wellcome to my conversor of currenty 

1- Pesos colombianos
2- Pesos Argentinos
3- Pesos mexicanos

Elija una Opcion """

opcion = int(input (menu))
if opcion == 1 :
    pesos = input("¿cuantos pesos colombianos tienes?:  ")
    pesos = float (pesos)
    valor_dolar = 3653 
    dolares = pesos / valor_dolar
    valor_rublo = 71.9
    rublos = dolares * valor_rublo
    rublos = round (rublos, 3)
    rublos = str(rublos)
    print("Tienes руб " + rublos + " rublos") 
elif opcion == 2:
    pesos = input("¿cuantos pesos argentinos tienes?:  ")
    pesos = float (pesos)
    valor_dolar = 65 
    dolares = pesos / valor_dolar
    valor_rublo = 71.9
    rublos = dolares * valor_rublo
    rublos = round (rublos, 3)
    rublos = str(rublos)
print("Tienes руб " + rublos + " rublos")
"""elif opcion == 3:
    pesos = input("¿cuantos pesos mexicanos tienes?:  ")
    pesos = float (pesos)
    valor_dolar = 24 
    dolares = pesos / valor_dolar
    valor_rublo = 71.9
    rublos = dolares * valor_rublo
    rublos = round (rublos, 3)
    rublos = str(rublos)
print("Tienes руб " + rublos + " rublos")"""
else:
 print ("Ingresa una opción correcta por favor")



