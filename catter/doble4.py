#si la compra es mayor a 100 soles optengo un descuento del 10%

#DECLARACION
nombre_del_cliente=""
monto=0.0

import os

#INPUT
nombre_del_cliente=str(os.sys.argv[1])
monto=float(os.sys.argv[2])

#PROCESSING
tiene_descuento=(monto>100)

if (monto>100):
    print("tiene 10% de descuento")
else:
    print("no tiene descuento")
