import random
import time

def busqueda_ingenua(lista, objetivo):
    
    #recorremos los valores de la lista
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0
        
    if limite_superior is 0:
        limite_superior = len(lista) -1
        
    punto_medio = (limite_inferior + limite_superior) // 2
    
    if lista[punto_medio] == objetivo :
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio -1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio + 1, limite_superior)
    
if __name__ == '__main__':
    
    conjunto_inicial: set()
    tamaño = 10000
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        
    lista = sorted(list(conjunto_inicial))    
        
    #medir el tiempo de busqueda ingenua
    inicio = time.time()
    for objetivo in lista:
        busqueda_ingenua(lista, objetivo)
    fin = time.time()
    
    #medir el tiempo de busqueda binaria
    inicio = time.time()
    for objetivo in lista:
        busqueda_binaria(lista, objetivo)
    fin = time.time()