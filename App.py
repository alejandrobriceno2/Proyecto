import requests as rq


import csv


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class App:
    None

    def cargar_API(self,link):
        informacion=rq.get(link).json()
        return informacion
    
    def start(self):
        None