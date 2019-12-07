#si la compra es mayor a 100 soles optengo un descuento del 10%

#DECLARACION
monto=0.0

import os

#INPUT

monto=float(os.sys.argv[1])

#PROCESSING
tiene_descuento=(monto>100)

if (monto<100):
    print("no tiene descuento")
if (monto>=100 and monto <=500):
    print("tiene 10% de descuento")
if (monto>500 and monto <=800):
    print("tiene 30% de descuento  mas un accesorio de regalo")

