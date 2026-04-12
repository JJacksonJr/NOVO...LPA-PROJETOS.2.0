import os 


os.system("cls")


def medidas(numero):

    km=numero / 1000

    hm=numero / 100

    dam=numero / 10

    dm=numero / 0.1

    cm=numero / 0.01

    mm=numero / 0.001

    return km,hm,dam,dm,cm,mm








n=float(input(" Digite um numero "))


km_,hm_,dam_,dm_,cm_,mm_=medidas(n)

print(f" {n}: o valores das medidas desse numero é:  Km:{km_}  hm:{hm_}  dam: {dam_}  dm:{dm_}  cm:{cm_} mm:{mm_}")