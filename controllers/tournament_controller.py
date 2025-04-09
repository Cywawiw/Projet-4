from tinydb import TinyDB, where
from models.tournament import Tournament


class TournamentController:
    """
    Controller to manage tournament-related operations.
    """

    def __init__(self, player_controller, tournament_file="data/tournaments.json"):
        """
        Initialize the TournamentController.

        Args:
            player_controller (PlayerController): Controller to manage players.
            tournament_file (str): Path to the JSON file for tournament storage.
        """
        self.db = TinyDB(tournament_file)
        self.tournaments_table = self.db.table("tournaments")
        self.player_controller = player_controller
        self.selected_tournament = None

    def add_tournament(self):
        """
        Add a new tournament by gathering input from the user.
        """
        print("\n[Add a Tournament]")
        name = input("Tournament Name: ").strip()
        location = input("Location: ").strip()
        start_date = input("Start Date (DD-MM-YYYY): ").strip()
        end_date = input("End Date (DD-MM-YYYY): ").strip()
        description = input("Description: ").strip()
        try:
            num_rounds = int(input("Number of Rounds (default is 4): ").strip() or 4)
        except ValueError:
            print("Invalid input. Setting the number of rounds to the default value of 4.")
            num_rounds = 4

        # List all players and allow user to select participants
        players = self.player_controller.load_players()
        if not players:
            print("No players available. Add players first.")
            return

        print("\nAvailable Players:")
        for idx, player in enumerate(players, start=1):
            print(f"{idx}. {player}")

        try:
            selected_indices = input("Enter player numbers separated by commas: ").strip()
            selected_indices = [int(i.strip()) - 1 for i in selected_indices.split(",")]
            selected_players = [players[i] for i in selected_indices]
        except (ValueError, IndexError):
            print("Invalid input. Failed to select players.")
            return

        # Create and save the tournament
        new_tournament = Tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            description=description,
            num_rounds=num_rounds,
            players=selected_players,
        )
        self.save_tournament(new_tournament)
        print(f"Tournament '{name}' added successfully with {len(selected_players)} players.")

    def list_tournaments(self):
        """
        Display a list of all tournaments stored in the database.
        """
        tournaments = self.load_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return

        print("\n[List of Tournaments]")
        for tournament in tournaments:
            print(f"{tournament.name} ({tournament.start_date} - {tournament.end_date})")

    def select_tournament(self):
        """
        Display a list of tournaments and allow the user to select one.

        Returns:
            Tournament: The selected tournament object or None if no valid selection.
        """
        tournaments = self.load_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return None

        print("\nAvailable Tournaments:")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name} - {tournament.location} - Rounds: {len(tournament.rounds)}")

        try:
            choice = int(input("Select a tournament by number: ")) - 1
            if 0 <= choice < len(tournaments):
                return tournaments[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        return None

    def display_tournament_rankings(self, tournament=None):
        """
        Display rankings for the given tournament. If no tournament is provided,
        prompt the user to select one.

        Args:
            tournament (Tournament): The tournament to display rankings for. If None, prompt the user.
        """
        if not tournament:
            tournament = self.select_tournament()
            if not tournament:
                print("No tournament selected. Please select a tournament first.")
                return

        print(f"\nRankings for Tournament '{tournament.name}':")
        sorted_players = sorted(
            tournament.players, key=lambda player: player.score, reverse=True
        )
        for i, player in enumerate(sorted_players, start=1):
            print(f"{i}. {player} - {player.score} points")

    def save_tournament(self, tournament):
        """
        Save a tournament to the database.

        Args:
            tournament (Tournament): The tournament to save.
        """
        self.tournaments_table.upsert(
            tournament.to_dict(),
            where("name") == tournament.name
        )

    def load_tournaments(self):
        """
        Load all tournaments from the database.

        Returns:
            list[Tournament]: A list of Tournament objects.
        """
        tournaments_data = self.tournaments_table.all()
        return [Tournament.from_dict(t) for t in tournaments_data]
