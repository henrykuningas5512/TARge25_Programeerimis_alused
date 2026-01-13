
""" 1.       Küsi kasutaja nime
    2.       Kui nimepikkus on vahemikus 5 – 10 (kaasa arvatud), siis tervita 3 korda
    3.       Muidu küsi kolm arvu ja tagasta nende summa. (Kordus)"""

import math


def nime_pikkus():
    name = input(print("Mis on teie nimi: "))
    if 5 <= len(name) <= 10:
        print(f"Tervist {name}!" *3)
    else:
        user_answer = []
        user_answer.append(print("Anna kolm arvu: "))
        print(sum(user_answer.append))

if __name__ == '__main__':
    nime_pikkus()

