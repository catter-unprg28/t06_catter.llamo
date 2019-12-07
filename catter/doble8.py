# dado un numero entero divididos entre 5, si el residuo da 0 mostrar el numero es divisor de 5

#DECLARACION
numero1=0

import os

#INPUT
numero1=int(os.sys.argv[1])

#PROCESSING
if (numero1 % 5 ==0):
    print("es divisor de 5")
else:
    print("no es divisor de 5")
