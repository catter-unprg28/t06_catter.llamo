#mostrar si un palillo de fosforo prende esta bueno

#declaracion
palillo_fosforo=""

import os

#INPUT
palillo_fosforo=str(os.sys.argv[1])

#PROCESSING

if (palillo_fosforo=="prende"):
    print("esta bueno")
else:
    print("esta mojado")
