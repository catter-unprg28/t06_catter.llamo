#mostrar multiplos de 3

#declaracion
numero=0

import os

#INPUT
numero=int(os.sys.argv[1])

#PROCESSING

if (numero%3==0):
    print("es multiplo")
if numero%3!=0:
    print("no es multiplo")

