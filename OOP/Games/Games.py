"""Game collection system with file saving."""


class Game:
    """Represent game model."""

    def __init__(self, name: str, genre: str, price: float, rating: float):
        """Class constructor."""
        self.name = name
        self.genre = genre
        self.price = price
        self.rating = rating

    def __str__(self):
        """Return formatted game information as string."""
        return f"{self.name} | {self.genre} | {self.price}€ | Rating: {self.rating}"

    def __eq__(self, other):
        """Compare two games by name (case-insensitive)."""
        if isinstance(other, Game):
            return self.name.lower() == other.name.lower()
        return False


class GameCollection:
    """Represent game collection."""

    def __init__(self, name: str, min_rating: float):
        """Class constructor."""
        self.name = name
        self.min_rating = min_rating
        self.games = []

    def game_exists(self, name: str) -> bool:
        """Check if a game already exists in the collection by name."""
        for game in self.games:
            if game.name.lower() == name.lower():
                return True
        return False

    def find_game(self, name: str):
        """Find and return a game by name, or None if not found."""
        for game in self.games:
            if game.name.lower() == name.lower():
                return game
        return None

    def can_add_game(self, game: Game) -> bool:
        """Check if a game can be added (not duplicate and meets rating requirement)."""
        if self.game_exists(game.name):
            return False
        return game.rating >= self.min_rating

    def add_game(self, game: Game):
        """Add a new game to the collection if allowed."""
        if self.can_add_game(game):
            self.games.append(game)
            print("Mäng lisatud!")
        else:
            print("Mängu ei saa lisada (duplikaat või madal rating)!")

    def remove_game(self, name: str):
        """Remove a game from the collection by name."""
        game = self.find_game(name)

        if game:
            self.games.remove(game)
            print("Mäng eemaldatud!")
        else:
            print("Mängu ei leitud!")

    def show_games(self):
        """Display all games in the collection."""
        if not self.games:
            print("Mänge pole lisatud.")
            return

        for game in self.games:
            print(game)

    def search_game(self, name: str):
        """Search and display games that match the given name."""
        found = False

        for game in self.games:
            if name.lower() in game.name.lower():
                print(game)
                found = True

        if not found:
            print("Mängu ei leitud!")

    def get_games_by_price(self):
        """Display all games sorted by price (ascending)."""
        for game in sorted(self.games, key=lambda g: g.price):
            print(game)

    def get_best_games(self):
        """Display games with the highest rating."""
        if not self.games:
            print("Mänge pole.")
            return

        max_rating = max(game.rating for game in self.games)

        for game in self.games:
            if game.rating == max_rating:
                print(game)

    def save_to_file(self):
        """Save all games to a text file."""
        with open("games.txt", "w", encoding="utf-8") as file:
            for game in self.games:
                file.write(f"{game.name};{game.genre};{game.price};{game.rating}\n")

        print("Andmed salvestatud faili!")

    def load_from_file(self):
        """Load games from a text file into the collection."""
        try:
            with open("games.txt", "r", encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(";")

                    if len(data) != 4:
                        continue

                    name = data[0]
                    genre = data[1]
                    price = float(data[2])
                    rating = float(data[3])

                    if not self.game_exists(name):
                        self.games.append(Game(name, genre, price, rating))

            print("Andmed laaditud failist!")

        except FileNotFoundError:
            print("Faili ei leitud. Uus fail luuakse.")


# ---------- PROGRAMM ----------

collection = GameCollection("Timmu Collection", 5.0)
collection.load_from_file()

while True:
    print("\n--- TIMMU KOLLEKTSIOONI MENÜÜ ---")
    print("1. Lisa mäng")
    print("2. Vaata kõiki mänge")
    print("3. Otsi mängu")
    print("4. Eemalda mäng")
    print("5. Sorteeri hinna järgi")
    print("6. Parimad mängud")
    print("7. Salvesta faili")
    print("8. Välju")

    choice = input("Sisesta valik: ")

    if choice == "1":
        try:
            name = input("Mängu nimi: ")
            genre = input("Žanr: ")
            price = float(input("Hind: "))
            rating = float(input("Hinnang (1-10): "))

            collection.add_game(Game(name, genre, price, rating))

        except ValueError:
            print("Viga! Sisesta õiged andmed.")

    elif choice == "2":
        collection.show_games()

    elif choice == "3":
        collection.search_game(input("Sisesta mängu nimi: "))

    elif choice == "4":
        collection.remove_game(input("Sisesta eemaldatav mäng: "))

    elif choice == "5":
        collection.get_games_by_price()

    elif choice == "6":
        collection.get_best_games()

    elif choice == "7":
        collection.save_to_file()

    elif choice == "8":
        print("Programm lõpetati.")
        break

    else:
        print("Vale valik!")
