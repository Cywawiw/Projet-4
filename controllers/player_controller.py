from tinydb import TinyDB, Query
from models.player import Player
import datetime

class PlayerController:
    """
    Controller to manage player-related operations.
    """
    def __init__(self, player_file="data/players.json"):
        self.db = TinyDB(player_file)
        self.players_table = self.db.table("players")

    def add_player(self):
        """Handle the addition of a new player."""
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        birth_date = input("Birth Date (DD-MM-YYYY): ")
        chess_id = input("Chess ID: ")
        try:
            # Validate date format
            datetime.datetime.strptime(birth_date, "%d-%m-%Y")
            new_player = Player(first_name, last_name, birth_date, chess_id)
            self.players_table.insert(new_player.to_dict())
            print(f"Player {new_player} added successfully.")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    def load_players(self):
        """Load all players from the database."""
        players_data = self.players_table.all()
        return [Player.from_dict(p) for p in players_data]

    def list_players(self):
        """Handle listing all players."""
        players = self.players_table.all()
        if not players:
            print("No players found.")
        else:
            sorted_players = sorted(players, key=lambda p: (p["last_name"], p["first_name"]))
            for player in sorted_players:
                print(f"{player['last_name']}, {player['first_name']} ({player['chess_id']})")

    def display_player_info(self):
        """Handle displaying player information."""
        chess_id = input("Enter the Chess ID: ")
        PlayerQuery = Query()
        result = self.players_table.search(PlayerQuery.chess_id == chess_id)
        if result:
            player_data = result[0]
            print(f"Name: {player_data['first_name']} {player_data['last_name']}")
            print(f"Birth Date: {player_data['birth_date']}")
            print(f"Chess ID: {player_data['chess_id']}")
        else:
            print("Player not found.")