"""
Klassi Harjutus

Loo klass maja andmete hoidmiseks (tubade arv, korrused, aadress)

Lisa käsklus maja andmete väljatrükiks

Lisa käsklus maja renoveerimiseks (muuda tubade arvu)

Lisa käsklus maja hindamiseks

Loo majast pärinev klass, demonstreeri polümorfismi toimimist.
"""

"""
Teemad:
1.	Klassi loomine (konstruktori ja väljadega)
a.	Vähemalt 2 välja ja 2 meetodit (ei lähe arvesse Getterid ja Setterid)

2.	Klassimuutuja 

3.	Pärilus 
a.	Vähemalt 1 väli ja 1 meetod
b.	Konstruktor vaikeväärtusega

4.	Katsetamine
a.	Kõik meetodid ja klassimuutuja

5.	Järjendi loomine
a.	Peab sisaldama kokku 100 isendit suhtarvuga 60/40
b.	Kasutama vähemalt üht meetodit kõigi peal
"""


class House:
    """Class representing a house."""

    house_count = 0

    def __init__(self, num_rooms, floors, address):
        """Create house."""
        self.__num_rooms = num_rooms
        self.floors = floors
        self.address = address
        House.house_count += 1

    def get_num_rooms(self):
        """Get number of rooms."""
        return self.__num_rooms

    def set_num_rooms(self, value):
        """Set number of rooms, must be non-negative."""
        if value < 0:
            print("Error: Number of rooms cannot be negative!")
        else:
            self.__num_rooms = value

    def get_total_houses(self):
        """Return total number of houses created."""
        return House.house_count

    def construction_cost(num_rooms, floors):
        """Estimate construction cost."""
        return num_rooms * 50000 + floors * 10000

    def __str__(self):
        """String representation for returning house data."""
        return f"House at {self.address}: {self.__num_rooms} rooms, {self.floors} floor(s)"

    def info(self):
        """Print house info."""
        print(str(self))

    def estimate_value(self):
        """Estimate house value."""
        value = House.construction_cost(self.__num_rooms, self.floors)
        print(f"Estimated value: €{value}")
        return value

    def renovate(self, new_rooms):
        """Renovate house (change rooms)."""
        self.set_num_rooms(new_rooms)
        print(f"House at {self.address} now has {self.__num_rooms} rooms")


class Residence(House):
    """Residence class, may include a garage."""

    def __init__(self, num_rooms=1, floors=1, address="Unknown", has_garage=False):
        """Create residence."""
        super().__init__(num_rooms, floors, address)
        self.has_garage = has_garage

    def info(self):
        """Print residence info."""
        garage_text = "Yes" if self.has_garage else "No"
        print(f"Residence at {self.address}: {self.get_num_rooms()} rooms, {self.floors} floor(s), garage: {garage_text}")


class Garden:
    """Garden that can belong to a house."""
    def __init__(self, size, has_pool=False):
        """Create garden and if has pool."""
        self.size = size
        self.has_pool = has_pool

    def info(self):
        """Print garden info"""
        pool_text = "with pool" if self.has_pool else "no pool"
        print(f"Garden: {self.size} sqm, {pool_text}")


if __name__ == "__main__":
    h1 = House(3, 2, "Pakase 5")
    h2 = House(7, 3, "Poska 12")

    h1.info()
    h2.info()
    h1.renovate(3)
    h1.estimate_value()

    r1 = Residence(2, 2, "Old Town 12", has_garage=False)
    r2 = Residence()
    r1.info()
    r2.info()

    garden1 = Garden(120, has_pool=True)
    garden1.info()

    print(f"Total houses created: {House.house_count}")
    print(f"Construction cost for 4 rooms, 2 floors: €{House.construction_cost(4,2)}")
