#Ingresar el sueldo de una persona
# si supera los 3000 soles mostrar un mensaje en pantalla indicando que debe pagar impuestos.

#declaracion
nombre=""
sueldo=0.0

import os

#INPUT
nombre=str(os.sys.argv[1])
sueldo=float(os.sys.argv[2])

#PROCESSING
pagara_impuestos=(sueldo>3000)

if (sueldo>3000):
    print(nombre,"PAGARA IMPUESTOS")
else:
    print(nombre,"NO PAGARA IMPUESTOS")
