#Actividad Bucle en grupo
#Delia Campos López

#Cada compañero dirá un número. Los guardarás en un diccionario, junto con el nombre del compañero.

diccionario ={"Franz":10,
             "Zayra":2,
             "Roel":3,
             "Andres":14,
             "Javier": 30}
print("Este es el diccionario", diccionario)

for i,j in diccionario.items():
    print("{0} eligió el número {1}". format(i,j))

numeros = diccionario.values()
lista = list(numeros)
maximo = max(lista)
minimo = min(lista)

print("El valor mínimo elegido fue: ",minimo)
print("El valor máximo elegido fue: ",maximo)
