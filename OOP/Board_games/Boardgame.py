"""Board games."""


class GameRound:
    """One game round with players and results."""

    def __init__(self, name, players, result_type, results):
        """Create a game round."""
        self.name = name
        self.players = players
        self.result_type = result_type
        self.results = results


class Player:
    """Stores player stats."""

    def __init__(self, name):
        """Create a player."""
        self.name = name
        self.games_played = 0
        self.wins = 0
        self.games = {}


class Game:
    """Stores rounds of one game."""

    def __init__(self, name):
        """Create a game."""
        self.name = name
        self.rounds = []


class Statistics:
    """Loads data and answers queries."""

    def __init__(self, filename):
        """Read file and build data."""
        self.rounds = []
        self.players = {}
        self.games = {}

        with open(filename, encoding="utf-8") as f:
            for line in f:
                game, players, rtype, results = line.strip().split(";")

                players = players.split(",")

                if rtype == "points":
                    results = list(map(int, results.split(",")))
                elif rtype == "places":
                    results = results.split(",")
                else:
                    results = results.strip()

                round_obj = GameRound(game, players, rtype, results)
                self.rounds.append(round_obj)

                if game not in self.games:
                    self.games[game] = Game(game)
                self.games[game].rounds.append(round_obj)

                for p in players:
                    if p not in self.players:
                        self.players[p] = Player(p)

                    self.players[p].games_played += 1
                    self.players[p].games[game] = self.players[p].games.get(game, 0) + 1

                winner = self._get_winner(round_obj)
                if winner:
                    self.players[winner].wins += 1

    def _get_winner(self, r):
        """Return winner of a round."""
        if r.result_type == "points":
            return r.players[r.results.index(max(r.results))]
        if r.result_type == "places":
            return r.results[0]
        return r.results

    def _game_most_wins(self, game):
        wins = {}
        for r in game.rounds:
            w = self._get_winner(r)
            wins[w] = wins.get(w, 0) + 1
        return max(wins, key=wins.get)

    def _game_most_frequent_winner(self, game):
        stats = {}
        for r in game.rounds:
            for p in r.players:
                stats.setdefault(p, [0, 0])[1] += 1
            stats[self._get_winner(r)][0] += 1
        return max(stats, key=lambda p: stats[p][0] / stats[p][1])

    def _get_loser(self, r):
        """Return last place player."""
        if r.result_type == "points":
            return r.players[r.results.index(min(r.results))]
        if r.result_type == "places":
            return r.results[-1]

    def _game_most_losses(self, game):
        losses = {}
        for r in game.rounds:
            if r.result_type == "winner":
                continue
            loser = self._get_loser(r)
            losses[loser] = losses.get(loser, 0) + 1
        return max(losses, key=losses.get)

    def _game_most_frequent_loser(self, game):
        stats = {}
        for r in game.rounds:
            if r.result_type == "winner":
                continue
            for p in r.players:
                stats.setdefault(p, [0, 0])[1] += 1
            stats[self._get_loser(r)][0] += 1
        return max(stats, key=lambda p: stats[p][0] / stats[p][1])

    def _game_record_holder(self, game):
        best_score = -1
        holder = None
        for r in game.rounds:
            if r.result_type != "points":
                continue
            for i, score in enumerate(r.results):
                if score > best_score:
                    best_score = score
                    holder = r.players[i]
        return holder

    def _game_player_amount(self, game):
        counts = {}
        for r in game.rounds:
            n = len(r.players)
            counts[n] = counts.get(n, 0) + 1
        return max(counts, key=counts.get)

    def _handle_player(self, parts):
        """Handle player queries."""
        player = self.players[parts[1]]

        if parts[2] == "amount":
            return player.games_played
        if parts[2] == "favourite":
            return max(player.games, key=player.games.get)
        if parts[2] == "won":
            return player.wins

    def _handle_game(self, parts):
        """Handle game queries."""
        game = self.games[parts[1]]
        action = parts[2]

        if action == "amount":
            return len(game.rounds)

        if action == "player-amount":
            return self._game_player_amount(game)

        if action == "most-wins":
            return self._game_most_wins(game)

        if action == "most-frequent-winner":
            return self._game_most_frequent_winner(game)

        if action == "most-losses":
            return self._game_most_losses(game)

        if action == "most-frequent-loser":
            return self._game_most_frequent_loser(game)

        if action == "record-holder":
            return self._game_record_holder(game)

    def get(self, path: str):
        """Handle query and return result."""
        parts = path.strip("/").split("/")

        if path == "/players":
            return list(self.players.keys())

        if path == "/games":
            return list(self.games.keys())

        if path == "/total":
            return len(self.rounds)

        if parts[0] == "total":
            return sum(1 for r in self.rounds if r.result_type == parts[1])

        if parts[0] == "player":
            return self._handle_player(parts)

        if parts[0] == "game":
            return self._handle_game(parts)


if __name__ == "__main__":
    stats = Statistics("Results.txt")

    print("Players:", stats.get("/players"))
    print("Games:", stats.get("/games"))
    print("Total:", stats.get("/total"))

    print("Joosep games:", stats.get("/player/joosep/amount"))
    print("Joosep wins:", stats.get("/player/joosep/won"))

    print("Chess amount:", stats.get("/game/chess/amount"))
    print("Chess most wins:", stats.get("/game/chess/most-wins"))
