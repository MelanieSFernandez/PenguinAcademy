####REGLAS
#Casilla ocupada, las siguientes en la misma condicion >2=celula muerta
#Casilla ocupada, nro de celulas <3=celula muere superpoblacion
#Casilla libre, =3 crelulas adyacentes = celula viva sgte turno

from random import randint

def definircelda():
    numero = randint(0,1)
    return numero

def crearmatriz(size):
    matriz = []
    for fila in range(size):
        matriz.append([])
        for columna in range(size):
            matriz[fila].append(definircelda())
    return matriz

def printmatriz(matriz):
    for fila in (matriz):
        print(fila)

matriz = crearmatriz(5)
matriz[0][1] = 1
printmatriz(matriz)


matriz = crearmatriz(5)
def modifmatriz(matriz,fila,columna):
    matriz[fila][columna]="-"
    return matriz

modifmatriz(matriz,2,2)
printmatriz(matriz)

def vidacelula(celula):
    if celula==1:
        return True
    else:
        return False

def cantvidacelula(matriz):
    size = len(matriz)
    contar = 0
    for fila in range(size):
        for columna in range(size):
            a= vidacelula(matriz[fila][columna])
            if a==True:
                contar = contar + 1
    return contar

matriz = crearmatriz(5)
printmatriz(matriz)
print(cantvidacelula(matriz),"celulas vivas")
