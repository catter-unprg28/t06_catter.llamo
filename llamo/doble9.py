# si el sol es muy fuerte y si supera los 38ºc, mostrar "precaucion puedes tener cancer a la piel"

#declaracion
nivel_de_grados_del_sol=0.0


import os

#INPUT
nivel_de_grados_del_sol=float(os.sys.argv[1])


#PROCESSING

if ( nivel_de_grados_del_sol>=38):
    print("puedes tener cancer a la piel")
else:
    print("estas fuera de tener cancer a la piel")
