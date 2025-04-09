from rich.console import Console
from rich.table import Table


class MainMenu:
    """
    Main menu interface for navigating different sections of the application.
    """

    def __init__(self, player_menu, tournament_menu, report_menu):
        """
        Initialize the MainMenu with all submenus.

        Args:
            player_menu (PlayerMenu): The player management menu.
            tournament_menu (TournamentMenu): The tournament management menu.
            report_menu (ReportMenu): The report generation menu.
        """
        self.player_menu = player_menu
        self.tournament_menu = tournament_menu
        self.report_menu = report_menu
        self.console = Console()

    def display_menu(self):
        """
        Display the main menu and handle user navigation.
        """
        while True:
            # Display the main menu with Rich library for better aesthetics
            self.console.print("[bold cyan]Main Menu[/bold cyan]")
            table = Table(title="Choose an option")
            table.add_column("Option", justify="center")
            table.add_column("Category", justify="center")
            table.add_row("1", "Players")
            table.add_row("2", "Tournaments")
            table.add_row("3", "Reports")
            table.add_row("4", "Exit")
            self.console.print(table)

            choice = input("Your choice: ").strip()

            match choice:
                case "1":
                    self.player_menu.display_menu()
                case "2":
                    self.tournament_menu.display_menu()
                case "3":
                    self.report_menu.display_menu()
                case "4":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
