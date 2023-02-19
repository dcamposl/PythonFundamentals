#Actividad Competidores Olimpicos
#Delia Campos López

#Crear un programa en Visual Studio que me permita saber cuál 
# es el competidor más veterano que ha recibido medalla (oro, plata o bronce)

import pandas as pd
import numpy as np

import csv 

datos = pd.read_csv("C:\\Users\\user\\Documents\\CursoPython\\PythonFundamentals\\athlete_events.csv")

#cuál es el competidor más veterano que ha recibido medalla (oro, plata o bronce)
old = datos[datos["Age"] == datos["Age"].max()]
print(old)

#cuál es el competidor más joven que ha recibido medalla de oro
gold = datos[datos["Medal"] == "Gold"]
young = gold[gold["Age"] == gold["Age"].min()]
print(young)

#competidor más ganador de la historia y crea un csv con toda su información.

medal = datos[datos["Medal"].notna()]
rep = medal.groupby(["Name"]).size().reset_index(name='conteo')
ord = rep.sort_values("conteo", ascending = False)
print(ord.head(1))

winner = datos[datos["Name"] == "Michael Fred Phelps, II"]
winner.to_csv("Competido_mas_ganador.csv", header=True)