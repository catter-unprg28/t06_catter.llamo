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

if ( pago>=300 and pago<=700):
    print("es un buen sueldo")
else:
    print("mal sueldo sueldo")

