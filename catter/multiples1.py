#Ingresar el sueldo de una persona
# si el sueldo es menor a 3000 soles mostrar un mensaje en pantalla sino pagara el 10%.

#declaracion
nombre=""
sueldo=0.0

import os

#INPUT
nombre=str(os.sys.argv[1])
sueldo=float(os.sys.argv[2])

#PROCESSING
pagara_impuestos=(sueldo>3000)

if(sueldo<3000):
    print(nombre,"NO PAGARA IMPUESTOS")
if(sueldo>3000 and sueldo<5000):
    print(nombre,"pagara 10% de su sueldo")
