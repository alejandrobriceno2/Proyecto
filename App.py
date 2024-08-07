import requests as rq
from Pelicula import Pelicula
from Especie import Especie
from Nave import Nave
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
#from Mision import Mision

import csv





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class App:
    peliculas_obj=[]
    personajes_obj=[]
    naves_obj=[]
    vehiculos_obj=[]
    especies_obj=[]
    planetas_obj=[]
    #misiones_obj=[]
    #cantidad_misiones=0






    def cargar_API(self,link):
        informacion=rq.get(link).json()
        return informacion
    
    def start(self):
        peliculas=self.cargar_API('https://www.swapi.tech/api/films/')
        self.crear_peliculas(peliculas['result'])
        self.crear_personajes()
        self.crear_especies()
        self.crear_planetas()
        self.crear_naves()
        self.crear_vehiculos()






        while True:
            menu=input('''ingrese una opcion del menu:
1. Ver Lista de Peliculas
2. Ver listado de todas las especies de la saga, ordenados por el ID
3. Ver lista de planetas
4. Buscar un personaje de la saga
5. Gráfico de cantidad de personajes nacidos en cada planeta
6. Gráficos de características de naves
7. Tabla estadística sobre naves
8. Construir Mision
9. Modificar Mision
10. Salir
--->:''')
            if menu=="1":
                for pelicula in self.peliculas_obj:
                    pelicula.mostrar_peliculas()

            elif menu=='2':
                None

            elif menu=='3':
                None

            elif menu=='4':
                None

            elif menu=='5':
                None

            elif menu=='6':
                None

            elif menu=='7':
                None

            elif menu=='8':
                None

            elif menu=='9':
                None

            elif menu=='10':
                None

            else:
                print('Ingrese una opcion contemplada en el menu: ')