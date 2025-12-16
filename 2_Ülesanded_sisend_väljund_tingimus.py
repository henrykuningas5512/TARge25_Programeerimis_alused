import math
from operator import length_hint

"""Ülesanne 1
Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala."""


"""def compute_rectangle():
    length = float(input("Sisesta ristküliku pikkus:"))
    width = float(input("Sisesta ristküliku laius:"))
    area = width * length
    circumference = 2 * (length + width)
    print(f"Antud ristküliku pindala on {area}")
    print(f"Ümbermõõt on {circumference}")

if __name__ == '__main__':
    # compute_rectangle()"""



"""Ülesanne 2
Koosta programm, mis küsib kasutajalt nime ja vanust ja väljastab ekraanile nimelise tervituse koos tekstiga, mis ütleb, kas tegemist on 7-18-aastase inimesega."""


"""def greet_by_name(name: str) -> str:
    return f"Tervist {name}!"

def verify_age(age: int) -> str:
    if 7 <= age <= 18:
        return "Oled 7-18 aastane"
    return "Sa ei ole 7-18 aastane"

if __name__ == '__main__':
    name = input("Sisesta oma nimi: ")
    age = int(input("Sisesta oma vanus aastates täisarvuna: "))
    greeting = greet_by_name(name)
    age_text = verify_age(age)
    print(greeting, age_text, sep="\n")"""




"""Ülesanne 3
Koosta lihtne kalkulaator. Kasutajalt küsitakse kaks arvu ja tehtemärk ning seejärel kuvatakse tehe koos vastusega. Näiteks:
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: 2+3=5"""

"""def calculate(num1: float, num2: float, operation: str) -> str:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "//":
        result = num1 // num2

    if result == "":
        return f"tundmatu tehe: {operation}"
    return f"{num1}{operation}{num2}={result}"


if __name__ == '__main__':
    first = float(input("Sisestage esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op =input("Sisestage tehe: ")
    print(f"Tulemus: {calculate(first, second, op)})")"""




"""Ülesanne 4
Eelmise ülesande alusel koostage programm M-Koer (Matemaatiline Koer), millele antakse samuti ette kaks arvu ja tehtemärk, kuid vastus ei kirjutata mitte arvulisel kujul, vaid esitatakse "haukudes". Igaks juhuks: tsükleid pole vaja kasutada, me pole neid veel õppinud.
Sisestage esimene arv: 2
Sisestage teine arv: 3
Sisestage tehe: +
Tulemus: auh auh auh auh auh"""

"""def dog_calculate(num1: float, num2: float, operation: str) -> str:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        result = num1 % num2
    elif operation == "//":
        result = num1 // num2

    if result == "":
        return f"URRRRR GRRRRRR: {operation}"
    return f"{round (result)* "auh "}"


if __name__ == '__main__':
    first = float(input("Sisestage esimene arv: "))
    second = float(input("Sisestage teine arv: "))
    op =input("Sisestage tehe: ")
    print(f"Tulemus: {dog_calculate(first, second, op)})")"""


"""Ülesanne 5
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja väljastab tulemuse Fahrenheiti kraadides. Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi? Proovi."""

"""def convert_to_fahrenheit(celsius_temperature: float) -> float:
    #convert given cel to f
    return celsius_temperature * 1.8 + 32

def convert_to_celsius(fahrenheit_temperature: float) -> float:
    #convert given f to cel
    return (fahrenheit_temperature - 32) / 1.8

if __name__ == '__main__':
    unit = input("Määra sisestava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuur Celsius kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_fahrenheit: .2f}F kraadi")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur Celsius kraadides: "))
        temperature_celsius = convert_to_fahrenheit(temperature_fahrenheit)
        print(f"{temperature_celsius}C on {temperature_fahrenheit: .2f}F kraadi")
    else:
        print(f"Sisestasid tundmatu temperatuuri ühiku - {unit}")
        print("Program toetab C - Celsius ja F - kraade")"""


"""Ülesanne 6
Loo programm, mis küsib kasutajalt ruutvõrrandi liikmete (ruutliige, lineaarliige, vabaliige) kordajad ning arvutab nende põhjal diskriminandi ja väljastab selle põhjal ruutvõrrandi lahendid. Nagu tead, võib lahendeid vastavalt diskriminandi väärtusele olla üks või kaks, kuid lahendid võivad ka puududa."""

"""def calculete_discriminant(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c

def solve_quadric_equasion(a, b, discriminant, useAddition):
    if useAddition:
        top = -b + math.sqrt(discriminant)
    else:
        top = -b - math.sqrt(discriminant)
    bottom = 2 * a
    return top/bottom

if __name__ == '__main__':
    print("Arvutame ruutvõrrandit!")
    a= float(input("sisesta ruutliige: "))
    if a == 0:
        print("Ruutliige ei tohi olla null.")
    else:
        b= float(input("sisesta lineaarliiga: "))
        c= float(input("sisesta vabaliige: "))
        discriminant = calculete_discriminant(a, b, c)
        if discriminant < 0:
            print("lahendid puuduvad")
        elif discriminant == 0:
            solution = solve_quadric_equasion(a, b, discriminant, True)
            print(f"lahendid on võrdsed: {solution}")
        else:
            solution1 = solve_quadric_equasion(a, b, discriminant, True)
            solution2 = solve_quadric_equasion(a, b, discriminant, False)
            print(f"lahendid on kaks: {solution1} ja {solution2}")"""



"""Ülesanne 7
Eestis kasutatav isikukood koosneb üheteistkümnest numbrist. Tutvu isikukoodi struktuuriga (https://et.wikipedia.org/wiki/Isikukood) ja kirjuta programm, mis analüüsib isikukoode ja väljastab võimalikult rohkem infot selle kohta (sünnikuupäev, sugu jne). Isikukoodi käsitlege kui sümbolite kogumit ehk sõnet (kuigi see koosneb numbritest), analüüsimiseks kasutage sõneoperatsioone (vt. käsiraamat). Kuna isikukoode on keeruline testimise ajal korduvalt sisestada, on alguses mõistlik sisestada erinevad isikukoodid ning kommenteerida vastavalt vajadusele ülearused välja, näiteks järgnevalt kasutatakse teisel real olevat isikukoodi:
#isikukood = "60201302715"
isikukood = "48008082727"
#isikukood = "31212230156"
[...]

Hiljem võib lisada isikukoodi küsimise kasutajalt.

Täiendusi:

    Vastavalt toodud isikukoodi tutvustavale artiklile võrdle esimest kümmet numbrit ja viimast numbrit (nn. kontrollnumbrit), et teha selgeks, kas isikukood on üldse kehtiv. Kuna isikukoodi võtame kui sõnet, aga seal olevaid arve on vaja korrutada, peame tegema tüübiteisenduse: sõnena oleva arvu peame teisendama täisarvuks (funktsioon "int()").
    Koosta funktsioon, mis ise automaatselt koostab kehtivaid isikukoode. Võimatud on näiteks isikukoodid vale kontrollnumbriga, kuid ka sellised, mis viitavad olematule kuupäevale (algusega "3950230...", mis tähendaks 30. veebruari) vms. Vali kas "ohutu" tee (ette on antud piirid, mis kehtivad igal juhul) või loo sisemised sõltuvused (stiilis "kui kuu on aprill, siis maksimaalsete päevade arv on 30")."""








"""Ülesanne 8

Eelmises peatükis koostasime programme, kus algandmed olid programmi teksti jäigalt sisse kirjutatud. Vali neist kaks ning lisa neile vajalike sisendandmete küsimine. Kuna tegemist on olukorraga, kus kasutaja võib andmete sisestamisel eksida (sisestada vale tüüpi andmeid, mis annavad programmi töötamisel vea, näiteks kirjutada arvu asemel teksti), püüa mõelda (ja internetist otsida) võimalusi, kuidas selliseid vigu vältida. """