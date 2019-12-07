# dado el numero de ejercicios resueltos en python, si el numero supera los 200 mostrar "aprobado"

#declaracion
numero=0


import os

#INPUT
numero=int(os.sys.argv[1])


#PROCESSING

if numero<=50:
    print("estas en peligro")
if numero>50 and numero<=100:
    print("tienes oportunidad")
if numero>100 :
    print("estas aprobado")



