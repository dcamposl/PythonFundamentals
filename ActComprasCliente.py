#ACtividad compras cliente 
#Delia Campos López

#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que se cargarán, que pueden cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingresa el monto 0.
#Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese 
# una nueva cantidad. Al finalizar, informar el total a pagar teniendo en cuenta que, 
# si las ventas superan el total de $1000, se debe aplicar un 10% de descuento.

i=1
total=0;
compra=0;

while i!=0:
    compras = int(input("Introduce el monto de tu compra: "))
    if compras < 0:
        print("Cantidad ingresada no valida, solo se aceptan monton positivos")
        total= total
    elif compras>0:
        total += compras
    else:
        i=0
        print("Termino de ingresar sus compras")
        


if total >1000:
    desc = total*0.10
    comprafinal = total - desc
    print("Su compra tiene un descuento del 10%")
    print("El total a pagar es de: ", comprafinal)
else:
    print("El total de su compra es:", total)
        
    