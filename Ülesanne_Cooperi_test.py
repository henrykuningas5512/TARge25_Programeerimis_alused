def hinda(meetrid: int, sugu: str) -> str:
    if sugu == "M":
        vaga_hea = 2800
        nork = 2000
    else:  # N
        vaga_hea = 2600
        nork = 1800

    if meetrid >= vaga_hea:
        return "väga hea"

    elif meetrid < nork:
        puudu = nork - meetrid
        return f"nõrk, järgmisest hindest puudu {puudu} m"

    else:
        puudu = vaga_hea - meetrid
        return f"rahuldav, järgmisest hindest puudu {puudu} m"


def main():
    failinimi = input("Sisestage failinimi: ")

    m_summa = 0
    n_summa = 0
    m_kogus = 0
    n_kogus = 0

    with open(failinimi, "r") as f:
        for line in f:
            meetrid, sugu = line.strip().split()
            meetrid = int(meetrid)

            tulemus = hinda(meetrid, sugu)
            print(f"{sugu} {meetrid} m, {tulemus}")

            # keskmise jaoks
            if sugu == "M":
                m_summa += meetrid
                m_kogus += 1
            else:
                n_summa += meetrid
                n_kogus += 1

    print("Keskmised:")

    if m_kogus > 0:
        m_keskmine = round(m_summa / m_kogus)
        print(f"M {m_keskmine} m, {hinda(m_keskmine, 'M')}")

    if n_kogus > 0:
        n_keskmine = round(n_summa / n_kogus)
        print(f"N {n_keskmine} m, {hinda(n_keskmine, 'N')}")


if __name__ == "__main__":
    main()