def evaluate(distance: int, gender: str) -> str:
    if gender == "M":
        very_good = 2800
        weak = 2000
    else:
        very_good = 2600
        weak = 1800

    if distance >= very_good:
        return "väga hea"

    elif distance < weak:
        missing = weak - distance
        return f"nõrk, järgmisest hindest puudu {missing} m"

    else:
        missing = very_good - distance
        return f"rahuldav, järgmisest hindest puudu {missing} m"


def main():
    filename = input("Sisestage failinimi: ")

    male_total = 0
    female_total = 0
    male_count = 0
    female_count = 0

    with open(filename, "r") as file:
        for line in file:
            distance, gender = line.strip().split()
            distance = int(distance)

            result = evaluate(distance, gender)
            print(f"{gender} {distance} m, {result}")

            # for averages
            if gender == "M":
                male_total += distance
                male_count += 1
            else:
                female_total += distance
                female_count += 1

    print("Keskmised:")

    if male_count > 0:
        male_avg = round(male_total / male_count)
        print(f"M {male_avg} m, {evaluate(male_avg, 'M')}")

    if female_count > 0:
        female_avg = round(female_total / female_count)
        print(f"N {female_avg} m, {evaluate(female_avg, 'N')}")


if __name__ == "__main__":
    main()
