#Actividad Avanzada Edad 
#Delia Campos López


#Hagamos un programa que le pida al usuario que ingrese dos nombres 
#con su respectivas edades y muestre quién de ellos es mayor.

print("Por favor ingresa 2 nombres con sus respectivas edades: ")
nombre1 = input("Ingresa el primer nombre: ")
edad1 = input("Ingresa su edad: ")
edad1=int(edad1)
nombre2 = input("Ingresa el segundo nombre: ")
edad2 = input("Ingresa su edad: ")
edad2=int(edad2)

print(edad1, edad2)

if edad1==edad2 and edad1>=18:
    print(nombre1, " y ", nombre2, " tienen la misma edad:", edad1, "años, y son mayores de edad")
elif edad1==edad2 and edad1<18:
    print(nombre1, " y ", nombre2, " tienen la misma edad:", edad1, "años, y son menores de edad")
elif edad1>edad2 and edad1>=18:
    print(nombre1, " es mayor que ", nombre2, ", ya que tiene :", edad1, "años, y es mayor de edad")
elif edad2>edad1 and edad1>=18:
    print(nombre2, " es mayor que ", nombre1, ", ya que tiene :", edad2, "años, y es mayor de edad")
elif edad1>edad2 and edad1<18:
    print(nombre1, " es mayor que ", nombre2, ", ya que tiene :", edad1, "años, y es menor de edad")
elif edad2>edad1 and edad1<18:
    print(nombre2, " es mayor que ", nombre1, ", ya que tiene :", edad2, "años, y es menor de edad")
else:
    print("Debes de ingresar una edad correcta")