#motrar si el cliente se apellida gonzales participa del sorteo de un carro

#DECLARACION
apellido_del_cliente=""

import os

#INPUT
apellido_del_cliente=str(os.sys.argv[1])

#PROCESSING
if (apellido_del_cliente=="gonzales"):
    print("participa del sorteo")
else:
   print("no participa del sorteo")
