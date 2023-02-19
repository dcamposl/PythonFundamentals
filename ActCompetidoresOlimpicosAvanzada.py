#Actividad Competidores Olimpicos
#Delia Campos López

#Crear un programa en Visual Studio que me permita saber cuál 
# es el competidor más veterano que ha recibido medalla (oro, plata o bronce)

import pandas as pd
import numpy as np

import csv 

datos = pd.read_csv("C:\\Users\\user\\Documents\\CursoPython\\PythonFundamentals\\athlete_events.csv")
datos

#Crear un programa en Visual Studio que me permita saber cuál es el competidor 
#más veterano que ha recibido medalla para los NOC´s MEX, COL y ARG (oro, plata o bronce) 

NOC1 = (datos[(datos.NOC=='MEX') | (datos.NOC=='COL') | (datos.NOC=='ARG')])
old = NOC1[NOC1["Age"] == NOC1["Age"].max()]
print(old)

#Crear un programa en Visual Studio que me permita saber cuál 
#es el competidor más joven que ha recibido medalla de oro para los NOC´s USA y CAN

NOC2 = (datos[(datos.NOC=='USA') | (datos.NOC=='CAN')])
gold = NOC2[NOC2["Medal"] == "Gold"]
young = gold[gold["Age"] == gold["Age"].min()]
print(young)

#Encuentra al competidor más ganador de la historia en medallas totales, medallas de oro, 
#medallas de plata y medallas de broce para los NOC´s USA, CHN y RUS. Crea un csv con toda su información.

NOC3 = (datos[(datos.NOC=='USA') | (datos.NOC=='CHN') | (datos.NOC=='RUS')])
medal = NOC3[NOC3["Medal"].notna()]
rep = medal.groupby(["Name"]).size().reset_index(name='conteo')
ord = rep.sort_values("conteo", ascending = False)
print(ord.head(1))

winner = datos[datos["Name"] == "Michael Fred Phelps, II"]
winner.to_csv("Competido_mas_ganador_NOC.csv", header=True)
