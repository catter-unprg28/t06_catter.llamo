# calcular el salario semanal de un trabajador

#declaracion
nombre,horas,precioH,pago="",0,0.0,0.0


import os

#INPUT
nombre=str(os.sys.argv[1])
horas=int(os.sys.argv[2])
precioH=float(os.sys.argv[3])

#PROCESSING
pago=horas*precioH

if ( pago>=100and pago<=200):
    print("es un sueldo minimo")
if ( pago>200 and pago<=400):
    print("es un sueldo promedio")
if ( pago>400 and pago<=800):
    print("es un buen sueldo")


