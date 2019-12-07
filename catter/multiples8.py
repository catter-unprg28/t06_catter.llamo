# dado un numero entero divididos entre 5, si el residuo da 0 mostrar el numero es divisor de 5

#DECLARACION
numero=0

import os

#INPUT
numero=int(os.sys.argv[1])

#PROCESSING
if (numero % 5 ==0):
    print("es divisor de 5")
if (numero % 5 !=0):
    print("invalido")
