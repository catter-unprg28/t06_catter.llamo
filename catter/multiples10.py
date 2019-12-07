# mostrar la edad e identificar si esta apto para recibir la pension 65

#DECLARACION
edad=0

import os

#INPUT
edad=int(os.sys.argv[1])

#PROCESSING
if (edad<65):
    print("no recibe pension")
if (edad>=65 and edad<70):
    print("recibe pension 65")
if (edad>=70 and edad<90)
    print("recibe pension 75")
