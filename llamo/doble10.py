# dado el numero de ejercicios resueltos en python, si el numero supera los 200 mostrar "aprobado"

#declaracion
numero=0


import os

#INPUT
numero=float(os.sys.argv[1])


#PROCESSING

if ( numero>200):
    print("etas aprobado")

else:
    print("etas desaprobado")
