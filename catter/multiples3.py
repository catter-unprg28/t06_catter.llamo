#mostrar si el semaforo esta en verde cruzar la calle

#DECLARACION
color_de_semaforo=""

import os

#INPUT
color_de_semaforo=str(os.sys.argv[1])

#PROCESSING
if (color_de_semaforo=="verde"):
    print("cruzar la calle")
if (color_de_semaforo=="amarillo"):
    print("esperar el cambio del color")
if (color_de_semaforo=="rojo"):
    print("no cruzar")
