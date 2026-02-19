def main():
    kliendid = int(input("Sisesta klientide arv: "))

    summa = 0
    lilled = 1
    loendur = 0

    while loendur < kliendid:
        summa += lilled
        lilled += 2
        loendur += 1

    print("Kingitavate lillede koguarv:", summa)

if __name__ == '__main__':
    main()

