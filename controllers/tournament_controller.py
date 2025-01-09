from models.tournament import Tournament
from tinydb import TinyDB, where
import datetime
from controllers.player_controller import PlayerController

class TournamentController:
    """
    Controller to manage tournament-related operations.
    """
    def __init__(self, tournament_file="data/tournaments.json"):
        self.db = TinyDB(tournament_file)
        self.tournaments_table = self.db.table("tournaments")
        self.selected_tournament = None

    def add_tournament(self):
        """Add a new tournament to the database."""
        print("\nAdd a Tournament")
        name = input("Tournament Name: ")
        location = input("Location: ")
        start_date = input("Start Date (DD-MM-YYYY): ")
        end_date = input("End Date (DD-MM-YYYY): ")
        description = input("Description: ")

        while True:
            try:
                num_rounds = int(input("Number of Rounds (default is 4): "))
                if num_rounds < 1:
                    raise ValueError("Number of rounds must be at least 1.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")

        player_controller = PlayerController()
        players = player_controller.load_players()

        if not players:
            print("No players available. Cannot create a tournament.")
            return

        print("\nAvailable Players:")
        for i, player in enumerate(players):
            print(f"{i + 1}. {player.first_name} {player.last_name} (ID: {player.chess_id})")

        selected_indices = input("Enter player numbers separated by commas: ").split(",")
        try:
            selected_players = [players[int(index) - 1].chess_id for index in selected_indices]
        except (ValueError, IndexError):
            print("Invalid selection. Aborting tournament creation.")
            return

        try:
            datetime.datetime.strptime(start_date, "%d-%m-%Y")
            datetime.datetime.strptime(end_date, "%d-%m-%Y")

            new_tournament = Tournament(
                name=name,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=description,
                num_rounds=num_rounds,
                players=selected_players
            )
            self.save_tournament(new_tournament)
            print(f"Tournament '{new_tournament.name}' created successfully with {len(selected_players)} players.")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

    def save_tournament(self, tournament):
        """Save a tournament to the database."""
        self.tournaments_table.upsert(
            tournament.to_dict(),
            where('name') == tournament.name
        )

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
        """Display available tournaments and allow user to select one."""
        tournaments = self.load_tournaments()
        if not tournaments:
            print("No tournaments available.")
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