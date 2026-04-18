



def lillede_arv():
    summa = 0
    arv = 1
    klientide_arv = int(input("Anna klientide arv: "))

    while True:
        summa += arv
        arv += 2
        klientide_arv -= 1
        if 0 == klientide_arv:
            return summa
            break



if __name__ == '__main__':
    print(lillede_arv())