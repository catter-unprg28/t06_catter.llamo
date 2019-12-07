#Ingresar la estatura de una persona, si es mayor a 1.64cm  es alto

#DECLARACION
estatura=0.0

import os

#INPUT
nombre=str(os.sys.argv[1])
estatura=float(os.sys.argv[2])

#PROCESSING

if (estatura>1.64):
    print("es alto")
else:
    print("no es alto")
