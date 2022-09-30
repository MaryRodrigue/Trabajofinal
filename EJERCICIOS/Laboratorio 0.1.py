#Laboratorio  3.1.1.12
year = int(input("Introduce un año:"))

if year >= 1582:
    if year % 4 != 0:
        print("Año Común")
    elif year % 100 != 0:
        print("Año Común")
    elif year % 400 != 0:
        print("Año Común")
    else:
        print("Año Bisiesto")
else:
    print("No está dentro del período del calendario Gregoriano")