"""Harjutus 4

Luua programm, mis küsib kasutajalt täisarvu ja väljastab arvu kohta järgmise info:

1. Teatab kasutajale kas tegu on paaris või paaritu arvuga.

2. Teatab kasutajale kas arv on suurem või väiksem kui 10.

3. Teatab kasutajale kas arv on suurem või väiksem kui 100.

4. Näitab kasutajale arvude ruute 1 kuni sisestatud arvuni.

5. Näitab kasutajale arvust ruutjuurt."""
import math
def arvu_info():
    "1."
    arv = int(input("Anna arvu: "))
    if arv % 2 == 0:
        print("paarisarv")
    else:
        print("paaritu arv")

    "2."
    if arv < 10:
        print("väksem kui 10")
    else:
        print("suurem kui 10")

    "3."
    if arv < 100:
        print("väksem kui 100")
    else:
        print("suurem kui 100")

    "4."
    for i in range(arv):
        print(f"{arv ** i}")

    "5."
    print(math.sqrt(arv))


if __name__ == '__main__':
    arvu_info()