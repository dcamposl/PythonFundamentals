#Actividad Funcion Cuadratica
#Delia Campos López

#Crea una función en la cual recibas como argumentos los 
# parámetros reales de una función cuadrática, y te regrese los valores de x1 y x2.

import math
import numpy as np




x1 = 0
x2 = 0

# Se crea la función 

def resolver_ecuacion_cuadrada():
    soluciones = []
    a=float(input("Ingresa el valor del coeficiente a: "))
    b=float(input("Ingresa el valor del coeficiente b: "))
    c=float(input("Ingresa el valor del coeficiente c: "))

    #Se calcula el discriminante
    disc = (b*b)-(4*a*c)

    if disc<0:
        print("La ecuación no tiene soluciones reales")
    else:
        raiz = math.sqrt(disc)
        x1 = (-b + raiz)/(2*a)
        soluciones.append(x1)
        x2 = (-b - raiz)/(2*a)
        soluciones.append(x2)
        print(f'Las soluciones son {x1} y {x2}.')

    return soluciones



print(resolver_ecuacion_cuadrada())
    

