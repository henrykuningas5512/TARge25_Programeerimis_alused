""" 1.     +  Küsi kasutaja nime ja vanust
    2.     +  Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
    3.       Muidu küsi kolm arvu ja nende summa
    4.       Teata kas said õige tulemuse."""
def saa_kastutaja_vanus():
    nimi = input("Mis on su nimi? ")
    vanus = int(input("Kui vana oled? "))

    if len(nimi) < vanus or len(nimi) < 5:
        for i in range(3):
            print(f"Tervsit {nimi}!")
    else:
        arv1 = int(input("Anna esimene arv: "))
        arv2 = int(input("Anna teine arv: "))
        arv3 = int(input("Anna kolmas arv: "))
        kasutaja_summa = int(input("Anna nende summa: "))
        tegelik_summa = arv1 + arv2 + arv3

        if kasutaja_summa == tegelik_summa:
            print(f"{tegelik_summa} on tõesti õige.")
        else:
           print(f"Vale, tegelik summa on {tegelik_summa}.")

if __name__ == '__main__':
    saa_kastutaja_vanus()
