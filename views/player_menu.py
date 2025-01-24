"""
Menu for managing players in the chess tournament application.
"""

from rich.console import Console
from rich.table import Table


class PlayerMenu:
    """
    Menu interface for managing players.
    """

    def __init__(self, player_controller):
        """
        Initialize the PlayerMenu with the player controller.

        Args:
            player_controller (PlayerController): Controller for managing players.
        """
        self.player_controller = player_controller
        self.console = Console()

    def display_menu(self):
        """
        Display the player management menu and handle user navigation.
        """
        while True:
            # Display the player menu with Rich library for better visuals
            self.console.print("[bold cyan]Player Menu[/bold cyan]")
            table = Table(title="Player Management")
            table.add_column("Option", justify="center")
            table.add_column("Action", justify="center")
            table.add_row("1", "Add a Player")
            table.add_row("2", "List All Players")
            table.add_row("3", "Display Player Info")
            table.add_row("4", "Back to Main Menu")
            self.console.print(table)

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    self.player_controller.add_player()
                case "2":
                    self.player_controller.list_players()
                case "3":
                    self.player_controller.display_player_info()
                case "4":
                    break
                case _:
                    print("Invalid choice. Please try again.")
