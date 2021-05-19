import random

def busqueda_binaria(lista, comienzo, final, objetivo):


    if comienzo > final:
        return False

    medio =(comienzo + final ) // 2 

    if lista[medio] == objetivo:
        return True

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)

    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)          

if __name__ == "__main__":
    tamaño_de_lista = int(input("De que tamaño sera la lista?  "))
    objetivo = int(input("Que numero quieres encontrar?  "))
    
    lista =sorted([random.randint(0,100) for i in range(tamaño_de_lista)])

    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo )
    print(lista)
     #print(f"El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista")
     #print(f’El elemento {objetivo}{" esta" if encontrado else " no esta"} en la lista’)
    print("El elemento " + str(objetivo) +  " esta en la lista " if encontrado else  (str(objetivo) + " no esta en la lista"))
    #print('El elemento {} {} enla lista'.format(objetivo, "esta"if objetivo else"no esta"))    