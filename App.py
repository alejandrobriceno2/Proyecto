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
        