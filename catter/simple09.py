# ingresar dos edades
# si el primero es mayor que el segundo

#DECLARACION
edad1=0
edad2=0

import os

#INPUT
edad1=int(os.sys.argv[1])
edad2=int(os.sys.argv[2])

#PROCESSING
if (edad1>edad2):
    print("la primera edad es mayor que la segunda")
