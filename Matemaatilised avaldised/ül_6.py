"""Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul
"x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni (20 kaasaarvatud).
Samuti loenda, mitu sellist kombinatsiooni leiti."""
from itertools import count

count = 0
for z in range(20):
    for y in range(20):
        for x in range(20):
            print(f"{x + 1} - {y + 1} - {z + 1}")
            count += 1

print(f"Kokku leiti {count} kombinatsiooni")




Lahendus peab olema tehtud funktsioonidega ja käivitatav

if __name__ == '__main__':
koodiblokis.

Esitada lahendus fail nimega KT1_omanimi_ÜL#
Lahenduses peab olema järgitud koodistiili ja pydoc tavasid.
--------------------------------
arvud = []
for i in range(3):
    arvud.append(int(input("Sisesta arv: ")))

vaikseim = min(arvud) * 2

valed = []

for i in range(1, vaikseim + 1):
    vastus = int(input(f"{i} ruut = "))
    if vastus != i  2:
        valed.append(i  2)

if len(valed) == 0:
    print("Kõik vastused õiged!")
else:
    print("Valed vastused, õiged ruudud olid:")
    for r in valed:
        print(r)
----------------------------------

import random

nimi = input("Nimi: ")
vanus = int(input("Vanus: "))

if vanus < 5:
    for i in range(3):
        print("Tere", nimi)
    print("Tubli väike kasutaja!")
else:
    tehted = []
    õiged = 0

    for i in range(len(nimi)):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        vastus = int(input(f"{a} + {b} = "))
        if vastus == a + b:
            õiged += 1
        tehted.append(a + b)

    print(f"Said {õiged} õigesti!")
-----------------------------------

nimi = input("Nimi: ")
vanus = int(input("Vanus: "))

meeleolud = []

for aasta in range(18, vanus + 1):
    print(f"Õnnitleme {aasta}. täisealisena veedetud aasta eest!")
    meeleolu = input("Mis oli selle aasta meeleolu? ")
    meeleolud.append(meeleolu)

meeleolud.sort(key=len)

print("Meeleolud pikkuse järjekorras:")
for m in meeleolud:
    print(m)
-------------------------

sugu = input("Sugu (m/n): ")
vanus = int(input("Vanus: "))

tervitused = []
eelmine = ""

for i in range(10):
    if sugu == "m":
        tervitus = f"Tere härra, vanus {vanus}"
    else:
        tervitus = f"Tere proua, vanus {vanus}"

    if tervitus != eelmine:
        print(tervitus)
        eelmine = tervitus

    if i % 3 == 0 or i == 9:
        tervitused.append(tervitus)

    vanus += 1

print("Järjendi eelviimased sõnad:")
for t in tervitused:
    print(t.split()[-2])

--------------------------------------
laused = []

while True:
    lause = input("Sisesta lause: ")
    sonad = lause.split()

    if len(sonad) < 5:
        laused.append(lause)
    else:
        for s in sonad:
            print(s)
        break

------------------------------------------
sona = input("Sisesta sõna: ")
n = int(input("Sisesta number: "))

if n > 10:
    print("Viga")
else:
    jarjend = []
    for i in range(1, n + 1):
        jarjend.append(sona * i)

    print("Viimane väärtus:", jarjend[-1])

-----------------------------------------------
while True:
    arv = int(input("Sisesta arv: "))
    astmed = []

    for i in range(2, 6):
        astmed.append(arv  i)

    import random
    valik = random.choice(astmed)
    vastus = int(input(f"Mis astmes on arv {valik}? "))

    if arv  vastus == valik:
        print("Õige!")
    else:
        print("Vale, õige aste oli:", astmed.index(valik) + 2)

    if input("Jätkata? (j/e): ") != "j":
        break

----------------------------------------------
arvud = []

while True:
    a = int(input("Sisesta arv: "))
    arvud.append(a)

    if a > 0:
        print("Proovi negatiivset")
    elif a < 0:
        print("Proovi positiivset")
    else:
        print("Õnnitleme! Pääsesid tsüklist.")
        break

arvud.sort(reverse=True)
print("Sisestatud arvud kahanevalt:")
for x in arvud:
    print(x)
--------------------------------------------