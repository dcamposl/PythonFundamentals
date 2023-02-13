#Actividad Operaciones Edad-Ecuaciones

#Delia Campos López

#1.-El doble de mi edad tiene 24 años, ¿cuántos años tengo? (x=?)

dobleEdad = 24
x = dobleEdad/2
print("Mi edad es: ", x)


#2.- A un tercio de la edad de mi hermana le disminuyo 15 años para tener la misma edad que yo. 
#Yo tengo 6 años. ¿Qué edad tiene ella? 
#(Escribir la ecuación correspondiente, despejar y calcular la nueva variable "y" de manera manual)


print("La Ecuación correspondiente es:")
print("(y/3) - 15 = Edad, donde Edad=6")
print("Despegando y :")
print("y = (Edad + 15)*3")

Edad = 6
y = (Edad + 15)*3

print("La edad de mi hermana es: ", y)


#3.-Determina quién es más grande (variables "x" y "y") utilizando if y else.

if x>y:
    print("Yo soy mayor a mi hermana")
elif x==y:
    print("Tengo la misma edad que mi hermana")
else:
     print("Mi hermana es mayor que yo")