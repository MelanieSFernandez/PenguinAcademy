####Dia5

from pprint import pprint

persona={}

persona={'nombre': 'Laura', 'edad': 16, 'profesion': 'estudiante'}
pprint(persona['nombre'])


for dicc1 in persona:
    print(persona[dicc1])


#####pedirporinternet
import requests
API_KEY = "595695c3"

respuesta = requests.get("http://www.omdbp1.com/?ap1key=595695c3&t=HarryPoter")
print(respuesta.text)
harry = respuesta.json()

import requests
API_KEY = "595695c3"

titulo = "Blade"
busqueda = "http://www.omdbp1.com/ap1key=" + API_KEY + "&t=" + titulo
print(busqueda)
pelicula = requests.get(busqueda).json()
