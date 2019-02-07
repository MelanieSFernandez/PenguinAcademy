print("que")

pregunta = "cosa"
print(pregunta)

nombre = "Melanie"
print("Hola", nombre)
print("Hola",nombre,"que tal?")

nombre = Melanie
edad = 21
print("Hola",nombre,"tenes",edad)

#Operaciones matematicas
num1 = 12
num2 = 12
num3 = num1 * num2
print(num3)
num2 = 11
num3 = num1 * num2
print(num3)

#Hacer una lista
person = ["Melanie",21,"estudiante"]
print(person)
person.append("escuchar musica")
print("Hola",person[0],"tenes", person[1],"sos", person[2], "te gusta", person[3])

#Definir el ult elemento
person = ["Lau", 13,"estudiante"]
print(person)
cantidad = len(person)
person.append("jugar")
print("Hola",person[0],"tenes", person[1],"sos", person[2], "te gusta", person[3])
cantidad2 = len(person)
print("El ultimo es", person[cantidad2-1])

##opcion 2
cantidad = len(persona)
indice=0
print(person[indice])
indice_ultimo = cantidad -1
print(person[indice_ultimo])

##opcion 3
print(person[-2])

#insertar-quitar
person.insert(0,"Ms")
print(person)
person.remove(0)
print(person)

#Loops
theme_list = ["variables","tipos","listas"]
for concept in theme_list:
    print("hoy se aprendio", concept)
    print("que gusto")

print("fin")

#secuencia_repeticion
for i in range(1,10):
    print(i)

for i in range(1,10,3):
    print(i)

for i in range(12):
    print("Hola")

##operacion_lista
number_list = [1,2,3,4,5,6]
suma = 0
for i in number_list:
    suma = suma + i
    print(suma)

number_list = [1,2,3,4,5,6]
mult = 1

for i in number_list:
    print(mult,"*", i)
    mult = mult * i
print(mult)

#FUNCIONES

def saludo():
    print("Hola")

saludo()
saludo()
saludo()
saludo()

def division(dividendo,divisor):
    return dividendo/divisor

division(20,5)
division(5,20)

def potencia(ent):
    return ent*ent

potencia(4)

def saludo2(nombre,edad=14):
    print("Hola",nombre,"tenes",edad)

saludo2("Mel")

def saludo3(nombre="",edad=""):
    print("Hola",nombre,"tenes",edad)

saludo3(nombre="Mel",edad=21)

def saludo(nombre,edad):
    print("Hola",nombre,"tenes",edad)

saludo("Aniel",24)
saludo("Marce",32)

def potenc(ent,pot):
    return ent**pot

potenc(2,5)

def potenc2(ent,pot):
    return ent**pot

potenc2(3,5)

def suma_list(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

print(suma_list([1,20, 87,3,4]))

def suma_list(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

print(suma_list([1,2,3,4,5]))

def sum(listas):
    c= 0          
    for i in 
  
#Temas_Dia_1    
"Hola" #string
50 #integer
50.0 #loaf
[] #lists
def saludo() #function

def cuadrado_lista(recibo):
    for numero in recibo:
        print(numero)
        print(numero*numero)
        
cuadrado_lista([1,2,3,4])   






def cuadrado_lista(recibo):
    nuevo_lista = []
    for numero in recibo:
        nuevo_lista.append(numero*numero)
        
    return nueva_lista
cuadrado_lista([1,2,3,4]) 
####CONDICIONALES

def puede_tomar(edad):
    if edad >=21:
        return True
    else:
        return False
puede_tomar(15)

if puede_tomar(12)==False:
    print("no puede tomar")
else:
    print("puede tomar")


def calif(nota):
    if nota >=70:
        return True
    else:
        return False

if calif(65):
    print("aprobado")
else:
    print("aplazado")

calif(65)

if calif(85):
    print("aprobado")
else:
    print("aplazado")

calif(85)

def edadtomar(edad):
    if edad >90:
        print("no recomendable")
    elif edad >=18:
        print("tomar,no comprar")
    elif edad >14:
        print("ilegal")
    else:
        print("bastante ilegal")

edadtomar(14)

def educacioninicial(clasifedad):
    if clasifedad >=18:
        print("ed universitaria")
    if clasifedad >=13:
        print("fin ed inicial")
    elif clasifedad <=5:
        print("jardin")
    elif clasifedad <=6:
        print("preescolar")
    elif clasifedad >=7:
        print("ed primaria")
    else:
        print("basarse en fecha de nacimiento")
educacioninicial(15)

def viveanimal(lista_animales):
lista_animales = ["perro","gato","caballo","tortuga","vaca","pinguino"]
    for animal in lista_animales:
        if animal=="perro":
            print("vive en la casa")
        elif animal=="gato":
            print("vive en la casa")
        elif animal=="caballo":
            print("no vive en la casa")
        elif animal=="tortuga":
            print("vive en la casa")
        elif animal=="vaca":
            print("ni sonhando")
        elif animal=="pinguino":
            print("espiritu del grupo")

print(viveanimal(lista_animales))

