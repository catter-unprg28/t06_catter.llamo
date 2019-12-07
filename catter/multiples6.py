#Ingresar el peso de 3 personas
#si la suma supera 300 kg entran a una dieta intensiva

#DECLARACION
peso1,peso2,peso3,total=0.0,0.0,0.0,0.0

import os

#INPUT
peso1=float(os.sys.argv[1])
peso2=float(os.sys.argv[2])
peso3=float(os.sys.argv[3])

#PROCESSING
total=peso1+peso2+peso3

if (total<300):
    print("no reciben dieta intensiva")
if (total>=300 and total<400):
    print("reciben dieta intensiva con 30% de descuento")
if (total>=400 and total<=500):
    print("gratis un mes de gym")
