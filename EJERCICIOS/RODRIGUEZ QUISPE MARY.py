#APLICACIÓN DE ÁREAS DE FIGURAS PLANAS 
print("Hola..." "\nEn esta aplicación podras hallar las áreas de 5 figuras planas")
operación = 0
while operación !=6:
    
    print("Estas son las opciones:\n")
    print("1.-Ractángulo\n2.-Cuadrado\n3.-Rombo\n4.-Triángulo\n5.-Círculo\n6.-Salir")
    operación= int(input("Elija la opción que desea realizar(escribe el número): "))

    if operación == 1:
        print("__ÁREA DE UN RECTÁNGULO__")
        base1=float(input("Ingrese la base del rectángulo: "))
        altura1=float(input("Ingrese la altura del rectángulo: "))

        area1=base1*altura1
                                     
        print("El área del rectángulo es: ",round(area1,2))

    elif operación == 2:
        print("__ÁREA DE UN CUADRADO__")
        lado=float(input("Ingrese el lado del cuadrado: "))

        area2=lado**2

        print("El área del cuadrado es: ",round(area2,2))

    elif operación == 3:
        print("_ÁREA DE UN ROMBO_")

        diagonal1=float(input("Ingrese la longitud de la diagonal mayor: "))
        diagonal2=float(input("Ingrese la longitud de la diagonal menor: "))

        area3= diagonal1*diagonal2/2

        print("El área del rombo es: ",round(area3,2))

    elif operación == 4:
        print("_ÁREA DE UN TRIÁNGULO_")
        base4=float(input("Ingrese la base del triángulo: "))
        altura4=float(input("Ingrese la altura del triángulo: "))

        area4=base4*altura4/2

        print("El área del triángulo es: ",round(area4,2))

    elif operación == 5:
        print("_ÁREA DE UN CÍRCULO_")
        radio=float(input("Ingrese el radio del círculo: "))

        area5=3.141592*(radio**2)

        print("El área del círculo es de: ",round(area5,2))
    else:
        break


#APLICACIÓN PARA CALCULAR MRU
print("Movimiento rectilíneo uniforme")
opción=0
while opción !=4:
    print("Siguientes opciones :")
    print("1.- Velocidad\n2.-Distancia\n3.-Tiempo\n4.-Para salir")
    
    opción=int(input("Según las opciones ¿Qué desea hallar?(escribe el número): "))
    if opción == 1:
        print("....Velocidad....")
        tiempo=float(input("Ingrese el tiempo(en segundos): "))
        distancia=float(input("Ingrese la distancia(en metros): "))
        velocidad=distancia/tiempo
        print("la velocidad es de: ",round(velocidad,2),"metros por segundo")
    if opción==2:
        print("....Distancia....")
        velocidad2=float(input("Ingrese la velocidad(en metros por segundos): "))
        tiempo2= float(input("Ingrese el tiempo(en segundos): "))
        distancia2=velocidad2*tiempo2
        print("La distancia será igual a: ",round(distancia2,2),"metros")
    if opción==3:
        print("....Tiempo....")
        velocidad3=float(input("Ingrese la velocidad(en metros por segundos): "))
        distancia3= float(input("Ingrese la distancia(en metros): "))
        tiempo3=distancia3/velocidad3
        print("El tiempo es de: ",round(tiempo3,2),"segundos")
    else:
         
        break