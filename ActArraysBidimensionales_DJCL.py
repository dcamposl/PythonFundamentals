#Actividad Arrays Bidimensionales
#Delia Campos López

import numpy as np

#1.- Crear una matriz 3x3 con valores de 0 a 8


a=np.reshape(np.array(range(0,9)),(3,3))

print("Esto es una matriz 3X3: ",a)

#2.- Crear una matriz identidad de 6x6 utilizando la función .identity()
Iden = np.identity(6)
print("Esto es una matriz identidad : ",Iden)