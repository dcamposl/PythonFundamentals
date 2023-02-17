#Actividad Bucle en grupo
#Delia Campos López

#Asigna un número aleatorio a tu compañero. 
# Los guardarás en un diccionario, junto con el nombre de tu compañero.

import random

A = [ ]
 
for i in range (5):
    A.append(random.randint(1, 100))
 
print(A)

diccionario ={"Franz":A[0],
             "Zayra":A[1],
             "Roel":A[2],
             "Andres":A[3],
             "Javier": A[4]}

print("Este es el diccionario", diccionario)

for i,j in diccionario.items():
    print("{0} eligió el número {1}". format(i,j))

numeros = diccionario.values()
lista = list(numeros)
maximo = max(lista)
minimo = min(lista)

print("El valor mínimo elegido fue: ",minimo)
print("El valor máximo elegido fue: ",maximo)

