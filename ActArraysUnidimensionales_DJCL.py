#Actividad Arrays Unidemsionales
#Delia Campos López

import numpy as np

#1.- Crea un vector utilizando la función np.array() con valores dentro del rango 3 al número que representa tu edad. 
#Por ejemplo, si usted tiene 30 años, el vector debería de contener los números 3, 4, 5, ... , 30.

edad=36
ini=3

#Opción 1: utilizando np.array

b=list(range(ini, edad+1))
c=np.array(b)
print("Esto es un vector utilizando la función np.array: ",c)

#Opción 2: utilizando np.arange

a1=np.arange(start=ini, stop=edad+1,step=1)
print("Esto es un vector utilizando la función np.arange: ",a1)


#2.- Crea un arreglo con los siguientes elementos: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

m=[0,1,2,3,4]
n=m+m
print("Esto es un arreglo: ",n)

#3.- Ordena de forma ascendente dicho arreglo utilizando la función .sort().
orden = np.sort(n)
print("Esto es un arreglo ordenado: ",orden)