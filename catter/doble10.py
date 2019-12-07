# mostrar la edad e identificar si esta apto para recibir la pension 65

#DECLARACION
edad=0

import os

#INPUT
edad=int(os.sys.argv[1])

#PROCESSING
if (edad>65):
    print("recibe pension")
else:
    print("no recibe pension")
