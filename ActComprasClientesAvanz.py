#ACtividad compras cliente 
#Delia Campos López

#Crear un programa que permita al usuario ingresar el tiempo dentro en un estacionamiento , 
#cortando el ingreso de datos cuando el usuario ingresa 0 minutos.

i=1
totaltiempo=0;
minutos=0;

while i!=0:
    minutos = int(input("Introduce el tiempo que estuviste en el estacionamiento (en minutos): "))
    if minutos < 0:
        print("Cantidad ingresada no valida, solo se aceptan tiempos positivos")
        totaltiempo= totaltiempo
    elif minutos>0:
        totaltiempo += minutos
    else:
        i=0
        print("Termino de ingresar su tiempo")
        print("El tiempo total de su estacionamiento es de: ", totaltiempo, " minutos")
        

import math 

tarifafija = 25
horaadicional = 15
totalpago = 0
if totaltiempo <=60:
    totalpago = tarifafija
    print("Su pago total es de: $", totalpago)
else:
    horas = math.ceil(totaltiempo/60)
    print("El tiempo total de su estacionamiento es de: ",horas, " horas")
    totalpago = tarifafija + horaadicional*(horas-1)
    print("Su pago total es de: $", totalpago)


if horas>8:
    print("Debido a que tu tiempo en horas supera las 8, se deberá pagar un extra de $200")
    totalpago = totalpago +200
    print("El total de tu pago es: $",totalpago)



        