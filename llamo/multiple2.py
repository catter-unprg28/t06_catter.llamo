#mostrar si un palillo de fosforo prende esta bueno

#declaracion
fosforo=""

import os

#INPUT
fosforo=str(os.sys.argv[1])

#PROCESSING

if (fosforo=="prende"):
    print("esta bueno")

if (fosforo=="no prende"):
    print("esta mojado")

if (fosforo=="intentalo otra ves "):
    print("esta a prueba")
