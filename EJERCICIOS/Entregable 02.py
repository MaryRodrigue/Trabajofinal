#print("1.Escribe un programa que solicite al usuario ingresar cuatro números para luego mostrar el promedio de los tres")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el tercer número: "))
num4=float(input("Ingrese el cuarto número: "))

promedio=(num1+num2+num3+num4)/4

print("\nEl promedio es: ", promedio)

#print("2.Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida")
Inv1=int(input("Ingrese el primer valor de la inversion: "))
Inv2=int(input("Ingrese el segundo valor de la inversion: "))
Inv3=int(input("Ingrese el tercer valor de la inversion: "))
PorcentTotal=Inv1 + Inv2 + Inv3
Porcent1= (Inv1 *100)//PorcentTotal
Porcent2= (Inv2 *100)//PorcentTotal
Porcent3= (Inv3 *100)//PorcentTotal
print ("El porcentaje de la primera inversion es: ",(Inv1 / PorcentTotal) * 100,"%")
print ("El porcentaje de la segunda inversion es: ",(Inv2 / PorcentTotal) * 100,"%")
print ("El porcentaje de la tercera inversion es: ",(Inv3 / PorcentTotal) * 100,"%")

#print("3. Calcular el sueldo de un empleado, ingrese los siguientes datos: nombre, horas de trabajo y el salario por hora. Luego incrementar el sueldo en 15%")
Nombre = input("Ingrese su nombre completo: ")
print(Nombre)
Horas=int(input("Ingrese el número de horas trabajadas: "))
SalarioPorHora=int(input("Ingrese el monto a pagar por hora:"))
IngresoBruto=(Horas * SalarioPorHora)
print("El ingreso sin aumento es: $",IngresoBruto,".")
Aumento=(15 * IngresoBruto)//100
print("El aumento es: $",Aumento,".")
Total=IngresoBruto+Aumento
print("El ingreso con aumento es: $",Total,".")

#print("4. Ingresar 2 números y luego escoger la operación que se quiere hacer con ellos (suma, resta, multiplicación o división) y reportar el resultado")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
print("\nEstas son las operaciones que hay:")
print("Suma=número1+número2\nResta=número1-número2\nMultiplicación=número1*número2\nDivición=número1/número2")
	
operación=input("\nIngrese la operación que desea hacer: ")
if operación =="suma":
    print("\nLa suma de los números es: ",num1+num2)
elif operación =="resta":
    print("\nLa resta de los números es: ",num1-num2)
elif operación =="multiplicación":
    print("\nLa multiplicación de los números es: ",num1*num2)

elif operación == "división":
    print("\nLa divición de los números es: ",num1/num2)
else:
    print("operación no disponible")

#print("4.Diseñe un algoritmo que lea tres números y determine el número mayor.")
num1=float(input("Ingrese el primer número: "))
num2=float(input("Ingrese el segundo número: "))
num3=float(input("Ingrese el segundo número: "))

print("\nEl número mayor es: ",max(num1,num2,num3))

#print("5.Diseñe un algoritmo que determine si un número es para o impar")
print("Determinamos si un número es par o impar")
número = float(input("Escriba un número:"))
if número%2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#print("6.	Elabore un algoritmo que permita calcular el área de un triángulo.")
#Área = (base * altura) /2
print("Par hallar el área del triángulo ingrese los siguientes datos")
base = float(input("La base del triángulo: "))
altura = float(input("La altura del triángulo :"))

print("El área del triángulo es:" ,base*altura/2)

#print("7.Diseñe un algoritmo que verifique si la cantidad de dígitos ingresados de un DNI es correcta o no (el DNI tiene 8 dígitos")
Dni=input("Ingrese su número de DNI: ")
	
num=len(Dni)
if num != 8:
    print("El número de DNI ingresado no es correcto") 
else:
	print("El número de DNI es Correcto")

#print("8 .Una tienda de música ha puesto a la venta DVD de diversos géneros con los precios que se describe en la siguiente tabla:")
print("Género","Precio unitario",sep="            ")
print("------------------------------")
print("Salsa(s)","S/. 56.00", sep="------->")
print("Rock(r)","S/. 63.00", sep="------->")
print("Pop(p)","S/. 87.00", sep="-------->")
print("Folclore(f)","S/. 120.50", sep="--->")

Salsa=56.00
Rock=63.00
Pop=87.00
Folclore=120.50

s=int(input("Ingrese el número de discos de Salsa que desea comprar: "))
r=int(input("Ingrese el número de discos de Rock que desea comprar: "))
p=int(input("Ingrese el número de discos de Pop que desea comprar: "))
f=int(input("Ingrese el número de discos de Folclore que desea comprar: "))
if p >= 1 >= 1 :
    print("¡Se ganó un poster por comprar discos de pop!")
else:
    print("¡Lo siento! No se ganó ningun poster")
if r >= 1 :
    print("¡Se ganó un poster por comprar discos de Rock!")
else:
    r < 1 
    print("¡Lo siento! No se ganó ningun poster")

PrecioTotal=Salsa+Pop+Rock+Folclore
Cantidad=s+r+p+f
if Cantidad >=11:
    PrecioTotal=((PrecioTotal)-((PrecioTotal * 10.2)//100))
    print("El total de su compra es: ",PrecioTotal,"Nuevos Soles.")
elif Cantidad >= 5:
    PrecioTotal=((PrecioTotal)-((PrecioTotal)//100))
    print("El total de su compra es: ",PrecioTotal,"Nuevos Soles.")
elif Cantidad== 4:
    PrecioTotal=((PrecioTotal)-((PrecioTotal*6)//100))
    print("El total de su compra es: ",PrecioTotal,"Nuevos Soles.")
else:
    Cantidad<4
    print("El total de su compra es: ",PrecioTotal,"Nuevos Soles.")

#print("9.	Diseñar un programa que permita calcular los salarios de los trabajadores de una empresa a partir de los siguientes datos:")
ho_tra=int(input("Ingrese sus horas trabajadas: "))
print("\nTurnos de trabajo:")
print("1) Mañana\n2) Tarde\n3) Noche")
turno=input("\nIngrese el número del turno en el que trabajó: ")

if turno == "1":
    sal1= ho_tra*37.0
    print("Su salaraio neto es de: ",round(sal1,2))
elif turno == "2":
    sal2=ho_tra*38.20
    print("Su salario neto es de: ",round(sal2,2))
else:
    sal3= ho_tra*38.50
    if sal3>=2000 and sal3<=5000:
        des1 = 15*sal3/100 + sal3
        print("Tiene un descuento del 15%\nSu salario neto es de: ",round(des1,2))
    elif sal3>=8000 and sal3<=10000:
        des2 = 17*sal3/100 + sal3
        print("Tiene un descuento del 17%\nSu salario neto es de: ",round(des2,2))
    else:
        print("Su salario neto es de: ",round(sal3,2))



