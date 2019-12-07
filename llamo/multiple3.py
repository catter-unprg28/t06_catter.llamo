#ingresar 3 notas de un alumno
#si el promedio es mayor o igual a 7 mostrar un msje "promocionado"

#declaracion
nota1=0
nota2=0
nota3=0
prom=0

import os

#INPUT
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])

#PROCESSING
prom=(nota1+nota2+nota3)/3


if (prom<7):
    print("no tiene oprtunidad")

if (prom>=7 and prom<=10.5):
    print("tienes oprtunidad")

if (prom>10.5):
    print("estas aprobado")




