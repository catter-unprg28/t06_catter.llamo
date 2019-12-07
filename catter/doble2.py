# mostrar el promedio de 3 notas
#si obtiene un minimo de 10.5 esta aprobado

#DECLARACION
nota1,nota2,nota3,prom=0.0,0.0,0.0,0.0

import os

#INPUT
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])

#PROCESSING
prom=(nota1+nota2+nota3)/3

if prom>10.5:
    print("esta aprobado")
else:
    print("no esta aprobado")
