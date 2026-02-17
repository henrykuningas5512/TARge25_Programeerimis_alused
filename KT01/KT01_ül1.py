""" 1.     +  Küsi kasutajalt 3 arvu
    2.     +  Väikseim arv korruta kahega
    3.     +  Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
    4.     +  Teata kas kasutaja vastas õigesti või valesti
    5.       Teata mitu korda kasutaja vastas õigesti."""

"""arv1 = int(input("Anna esimene number: "))
arv2 = int(input("Anna teine number: "))
arv3 = int(input("Anna kolmas number: "))"""

arvud = []
õigesti = 0
for i in range(3):
    arv = int(input(f"Anna {i+1}. arv: "))
    arvud.append(arv)

min_arv = min(arvud)
tulemus = min_arv * 2

for i in range(1, tulemus + 1):
    kasutaja_vastus = int(input(f"Mis on {i} ruut?"))
    tegelik_vastus = i ** 2
    if kasutaja_vastus == tegelik_vastus:
        print("õige")
        õigesti += 1
    else:
        print("vale")

print(f"Said õigesti {õigesti}/{i}st korda.")
    



