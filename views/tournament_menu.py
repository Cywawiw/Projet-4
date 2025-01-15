class TournamentMenu:
    """
    View to display the tournament menu and handle user interactions.
    """
    def __init__(self, tournament_controller, round_controller):
        self.tournament_controller = tournament_controller
        self.round_controller = round_controller

    def display_menu(self):
        """Display the tournament menu options."""
        while True:
            print("\nTournaments")
            print("1. Add a tournament")
            print("2. List tournaments")
            print("3. Select a tournament")
            print("4. Create a round")
            print("5. End current round")
            print("6. Display rounds")
            print("7. Back to main menu")
            choice = input("Choose an option: ")

            match choice:
                case "1":
                    self.tournament_controller.add_tournament()
                case "2":
                    self.tournament_controller.list_tournaments()
                case "3":
                    self.select_tournament()
                case "4":
                    self.round_controller.create_round()
                case "5":
                    self.round_controller.end_round()
                case "6":
                    self.round_controller.display_rounds()
                case "7":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def select_tournament(self):
        """Select a tournament and set it in the RoundController."""
        selected_tournament = self.tournament_controller.select_tournament()
        if selected_tournament:
            self.round_controller.set_tournament(selected_tournament)

    def display_tournaments(self, tournaments):
        """Display a list of tournaments."""
        if not tournaments:
            print("No tournaments available.")
            return

        print("\nAvailable Tournaments:")
        for i, t in enumerate(tournaments):
            print(f"{i + 1}. {t.name} - {t.location} - Rounds: {len(t.rounds)}")
