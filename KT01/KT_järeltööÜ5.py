"""Harjutus 5

Kausitäis paprikasuppi jahtub minuti jooksul 19% võrra supi ja ruumi temperatuuride vahest.

Koostage programm, mis küsib sööjalt supi algtemperatuuri ja toatemperatuuri (just sellises järjekorras) ning väljastab, milline on supi täisarvuni ümardatud  temperatuur 10 minuti pärast.

Ümardamiseks saab kasutada funktsiooni round.

Eeldame, et supi algtemperatuur on väiksem kui 100 kraadi ja toatemperatuur on üle nulli."""
import math

def supp():

    supp_temp = int(input("Sisesta suppi algtemperatuur: "))
    toa_temp = int(input("Sisesta toa algtemperatuur: "))
    for i in range(10):
        vahe = supp_temp - toa_temp
        supp_temp = supp_temp - vahe*0.19
    return round(supp_temp)


if __name__ == '__main__':
    print(supp())