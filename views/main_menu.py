class MainMenu:
    """
    Main menu of the chess tournament program.
    """
    def __init__(self, player_menu, tournament_menu, round_menu):
        self.player_menu = player_menu
        self.tournament_menu = tournament_menu
        self.round_menu = round_menu

    def display_menu(self):
        """Display the main menu options."""
        while True:
            print("\nMain Menu")
            print("Choose an option to access the category:")
            print("1. Players")
            print("2. Tournaments")
            print("3. Rapports")
            print("4. Exit")
            choice = input("Your choice: ")

            match choice:
                case "1":
                    self.player_menu.display_menu()
                case "2":
                    self.tournament_menu.display_menu()
                case "3":
                    print("not available")
                case "4":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
