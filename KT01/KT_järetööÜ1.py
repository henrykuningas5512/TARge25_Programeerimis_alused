"""Harjutus 1

Mantra on silp, sõna, lause või heli, mida kasutatakse paljudes idamaistes religioonides mediteerimisel.

Mantrat korratakse nii kaua kui vajalikuks peetakse.



Koostada programm, mis

1.küsib kasutajalt lause, mida ta soovib mantrana kasutada,

2.küsib kasutajalt, mitu korda ta soovib mantrat korrata,

3.väljastab sama arv kordi ekraanile kasutaja sisestatud mantra."""

def arv():
    mantra = input("Siseta oma mantra: ")
    mantra_kogus = int(input("Mitu korda tahad korrata mantrat: "))
    for i in range(mantra_kogus - 1):
        print(mantra)
    return mantra



if __name__ == '__main__':
    print(arv())