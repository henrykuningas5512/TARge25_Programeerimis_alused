"""Harjutus 2

1.       Loo programm, kus kasutaja peab sisestama täisarve, mis on suuremad eelnevast sisestusest samas ei tohi olla liiga palju suuremad

2.       Piirid kehtesta juhuarvudega programmi töö käigus. Veendu, et piirid võimaldavad korrektset sisestust

3.       Programm peab lõppema kui eksitakse 3 korda või järgmine sisestus peab olema suurem kui 100

4.       Prindi programmi töö kokkuvõte"""
from random import randint


def full_number():
    tries = 0
    old_user_number = 0
    while True:
        user_number = int(input("Sisesta täisarv mis on vahemikus: "))
        minimum = randint(1, 10)
        maximum = randint(10, 20)
        if minimum + old_user_number < user_number < maximum + old_user_number:
            print("õige")
        elif tries == 2:
            print(f"vale {minimum + old_user_number} ja {maximum + old_user_number} vahel pidi olema.")
            break
        elif (minimum + old_user_number)  < 100:
            print(f"number läks üle 100")
            break
        else:
            tries += 1
            print(f"vale {minimum + old_user_number} ja {maximum + old_user_number} vahel pidi olema.")
        old_user_number = user_number


if __name__ == '__main__':
    full_number()