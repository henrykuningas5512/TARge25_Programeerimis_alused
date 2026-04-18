"""Harjutus 2
Koostada programm, mis

•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);

•arvutab while-tsükli abil lillede koguarvu, mida pood kingib;

•väljastab saadud lillede arvu ekraanile.



Vihje: lillede koguarvust võib mõelda kui summast, milles liidetavad on paaritud arvud alates 1 kuni esimese paaritu arvuni, mis pole suurem kui klientide arv.

Näiteks, kui kasutaja sisestas 7, siis paaritute arvude summa on 16, sest 1 + 3 + 5 + 7 = 16.

Kui kasutaja sisestas 8, siis on summaks samuti 16, sest 1 + 3 + 5 + 7 = 16."""

def lillede_arv():
    summa = 0
    arv = 1
    klientide_arv = int(input("Anna klientide arv: "))

    while arv <= klientide_arv:
        summa += arv
        arv += 2

    return summa



if __name__ == '__main__':
    print(lillede_arv())