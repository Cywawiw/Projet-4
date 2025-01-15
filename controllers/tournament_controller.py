from models.tournament import Tournament
from tinydb import TinyDB, where
import datetime
from models.player import Player
from controllers.player_controller import PlayerController

class TournamentController:
    """
    Controller to manage tournament-related operations.
    """
    def __init__(self, player_controller, tournament_file="data/tournaments.json"):
        self.player_controller = player_controller
        self.db = TinyDB(tournament_file)
        self.tournaments_table = self.db.table("tournaments")

    def add_tournament(self):
        """Add a new tournament."""
        print("\nAdd a Tournament")
        name = input("Tournament Name: ")
        location = input("Location: ")
        start_date = input("Start Date (DD-MM-YYYY): ")
        end_date = input("End Date (DD-MM-YYYY): ")
        description = input("Description: ")
        num_rounds = input("Number of Rounds (default is 4): ") or 4

        try:
            datetime.datetime.strptime(start_date, "%d-%m-%Y")
            datetime.datetime.strptime(end_date, "%d-%m-%Y")


            players = self.player_controller.load_players()
            if not players:
                print("No players available. Please add players first.")
                return

            print("\nAvailable Players:")
            for i, player in enumerate(players):
                print(f"{i + 1}. {player.first_name} {player.last_name} (ID: {player.chess_id})")

            player_indices = input("Enter player numbers separated by commas: ")
            selected_players = [players[int(i) - 1] for i in player_indices.split(",")]


            valid_players = [
                player if isinstance(player, Player) else Player.from_dict(player.to_dict())
                for player in selected_players
            ]


            new_tournament = Tournament(
                name=name,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=description,
                num_rounds=int(num_rounds),
                players=valid_players
            )
            self.save_tournament(new_tournament)
            print(f"Tournament '{new_tournament.name}' added successfully with {len(valid_players)} players.")
        except ValueError:
            print("Invalid input. Please check the date formats and player numbers.")

    def save_tournament(self, tournament):
        """Save a tournament to the database."""
        tournament_data = tournament.to_dict()
        self.tournaments_table.upsert(
            tournament_data, where("name") == tournament.name
        )
        print(f"Tournament '{tournament.name}' saved successfully.")
    def list_tournaments(self):
        """List all tournaments."""
        tournaments = self.tournaments_table.all()
        if not tournaments:
            print("No tournaments found.")
        else:
            for tournament in tournaments:
                print(f"{tournament['name']} - {tournament['location']} - Rounds: {tournament['num_rounds']}")

    def load_tournaments(self):
        """Load all tournaments from the database."""
        tournaments_data = self.tournaments_table.all()
        return [Tournament.from_dict(t) for t in tournaments_data]

    def select_tournament(self):
        """Select a tournament from the database."""
        tournaments = self.load_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return None

        print("\nAvailable Tournaments:")
        for i, tournament in enumerate(tournaments):
            print(f"{i + 1}. {tournament.name} - {tournament.location} - Rounds: {len(tournament.rounds)}")

        try:
            choice = int(input("Select a tournament by number: ")) - 1
            if 0 <= choice < len(tournaments):
                selected_tournament = tournaments[choice]
                print(f"Tournament '{selected_tournament.name}' selected.")
                return selected_tournament
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return None

        print("Available Tournaments:")
        for i, t in enumerate(tournaments):
            print(f"{i + 1}. {t.name} - {t.location}")

        try:
            choice = int(input("Select a tournament by number: ")) - 1
            if 0 <= choice < len(tournaments):
                self.selected_tournament = tournaments[choice]
                print(f"Tournament '{self.selected_tournament.name}' selected.")
                return self.selected_tournament
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        return None

    def display_tournament_players(self):
        """Display the list of players for a specific tournament."""
        tournaments = self.load_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return

        print("Available Tournaments:")
        for i, tournament in enumerate(tournaments):
            print(f"{i + 1}. {tournament.name}")

        try:
            tournament_index = int(input("Select a tournament by number: ")) - 1
            if tournament_index < 0 or tournament_index >= len(tournaments):
                raise IndexError

            tournament = tournaments[tournament_index]

            if not tournament.players:
                print(f"No players registered for tournament '{tournament.name}'.")
                return

            print(f"Players in Tournament '{tournament.name}':")
            for player_id in tournament.players:
                print(player_id)
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")