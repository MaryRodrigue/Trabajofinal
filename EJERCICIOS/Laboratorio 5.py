#print ("Laboratorio 3.1.1.11")
ingreso = float(input("Ingreso anual:"))

if ingreso < 85528:
   impuesto = 0.18 * ingreso - 556.02
else:
    impuesto = 14839.02 + 0.32 * (ingreso - 85528)   

impuesto = round (impuesto, 0)
print ("el impuesto es:", round(impuesto,0), "pesos")