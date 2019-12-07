# mostrar en ciclo esta persona

#declaracion
edaad=0


import os

#INPUT
edad=int(os.sys.argv[1])


#PROCESSING

if (edad>0 and edad<=4):
    print("se encuentra en la infancia")
if (edad>4 and edad<=12):
    print("se encuentra en la niñez")
if (edad>12 and edad<=17):
    print("se encuentra en la adolescencia")
if (edad>17 and edad<=25):
    print("se encuentra en la juventud")
if (edad>26 and edad<=35):
    print("se encuentra en la adultez")

