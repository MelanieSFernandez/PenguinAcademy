class dino:
    def __init__(self, un_nombre="",un_color="verde"):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy", self.nombre, "mi cuerpo es", self.color)

    def rugir(self, rugido):
        #print(self)
        #print(rugido)
        print("RAWR!!!!!!",rugido)

    def cambiar_color(self,un_color):
        self.color1 = un_color
    def que_color(self,un_color):
        print("El color de dino es", self.color1)

pepito = dino("Pepe","Verde")
print(pepito.nombre)
print(pepito.color1)
pepito.rugir("RAWR!!!!!!!!")
pepito.cambiar_color("amarillo")

class persona:
    def __init__(self, un_nombre="", una_edad="", una_profesion=""):
        self.nombre = un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        print("Hola, mi nombre es",self.nombre,"mi edad es",self.edad,"y mi trabajo es ser",self.profesion)

    def cumple(self):
        self.edad = self.edad + 1
        return self.edad

lore = persona("Lorena",25,"medico")
lore.cumple()
print(lore.edad)


