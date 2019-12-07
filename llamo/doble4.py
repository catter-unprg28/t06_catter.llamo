#demotrar si un año es bisiesto

#declaracion
fecha=0

import os

#INPUT
fecha=int(os.sys.argv[1])

#PROCESSING


if (fecha%4==0 and fecha%100!=0):
    print("el año, es un año bisiento")
else:
    print("el año, no es un año bisiento")


