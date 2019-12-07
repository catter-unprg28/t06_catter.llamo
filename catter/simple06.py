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

if (total>300):
    print("reciben una dieta intensiva")
