#This is a currency converter
def conversor(tipo_pesos,valor_dolar,valor_rublo):
    pesos = input("¿cuantos pesos "   +  tipo_pesos + " tienes?:  ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    rublos = dolares * valor_rublo
    rublos = round (rublos, 3)
    rublos = str(rublos)
    print("Tienes руб " + rublos + " rublos") 



menu = """
Wellcome to my conversor of currenty 

1- Pesos colombianos
2- Pesos Argentinos
3- Pesos mexicanos

Elija una Opcion """
opcion = int(input (menu))
if opcion == 1:
    conversor("colombianos",3875,71)
elif opcion == 2:
    conversor("Argentinos",65,71)
elif opcion == 3:
    conversor("Mexicanos",24,71)
else:
    print ("Ingresa una opción correcta por favor")