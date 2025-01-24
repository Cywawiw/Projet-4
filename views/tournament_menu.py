from rich.console import Console
from rich.table import Table


class TournamentMenu:
    """
    View to display the tournament menu and handle user interactions.
    """
    def __init__(self, tournament_controller, round_controller):
        self.tournament_controller = tournament_controller
        self.round_controller = round_controller
        self.console = Console()

    def display_menu(self):
        """Display the tournament menu options."""
        while True:
            self.console.print("[bold cyan]Tournament Menu[/bold cyan]")
            table = Table(title="Tournament Management")
            table.add_column("Option", justify="center")
            table.add_column("Action", justify="center")
            table.add_row("1", "Add a Tournament")
            table.add_row("2", "List Tournaments")
            table.add_row("3", "Select a Tournament")
            table.add_row("4", "Create a Round")
            table.add_row("5", "End Current Round")
            table.add_row("6", "Display Rounds")
            table.add_row("7", "Display Rankings")
            table.add_row("8", "Back to Main Menu")
            self.console.print(table)

            choice = input("Choose an option: ").strip()

            match choice:
                case "1":
                    self.tournament_controller.add_tournament()
                case "2":
                    self.tournament_controller.list_tournaments()
                case "3":
                    self.round_controller.set_tournament(
                        self.tournament_controller.select_tournament()
                    )
                case "4":
                    self.round_controller.create_round()
                case "5":
                    self.round_controller.end_round()
                case "6":
                    self.round_controller.display_rounds()
                case "7":
                    self.tournament_controller.display_tournament_rankings()
                case "8":
                    break
                case _:
                    self.console.print("[red]Invalid choice. Please try again.[/red]")
