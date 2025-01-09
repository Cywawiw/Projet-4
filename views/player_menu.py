class PlayerMenu:
    """
    View to display the player menu and handle user interactions.
    """
    def __init__(self, player_controller):
        self.player_controller = player_controller

    def display_menu(self):
        """Display the player menu options."""
        while True:
            print("\nPlayer Menu")
            print("1. Add a Player")
            print("2. List All Players")
            print("3. Display Player Info")
            print("4. Back to Main Menu")
            choice = input("Choose an option: ")

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
