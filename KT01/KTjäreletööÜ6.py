"""Harjutus 6

1.       Loo programm, mis küsib kasutaja ees ja perekonnanime.

2.       Teatab kumb on pikem kas ees või perekonnanimi

3.       Niimitu korda tervitab lühemat nime pidi"""

def nimede_pikkus():
    eesnimi = input("Sisesta oma eesnimi: ")
    perekonnanimi = input("Sisesta oma perekonnanimi: ")
    if len(eesnimi) < len(perekonnanimi):
        print("Perekonnanimi on pikkem")
        for i in range(len(perekonnanimi) - len(eesnimi)):
            print(eesnimi)
    else:
        print("Eesnimi on pikkem")
        for i in range(len(eesnimi) - len(perekonnanimi)):
            print(perekonnanimi)



if __name__ == "__main__":
    nimede_pikkus()