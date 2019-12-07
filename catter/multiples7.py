#Ingresar la estatura de una persona, si es mayor a 1.64cm  es alto

#DECLARACION
estatura=0.0

import os

#INPUT
estatura=float(os.sys.argv[2])

#PROCESSING

if (estatura<1.58):
    print("es chato")
if (estatura>=1.58 and estatura<1.65):
    print("estatura promedio")
if (estatura>=1.65 and estatura<1.85):
    print("es alto")
