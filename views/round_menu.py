class RoundMenu:
    def __init__(self, round_controller):
        self.round_controller = round_controller

    def display_menu(self):
        """Display the round menu options."""
        print("\nRound Menu")
        print("1. Create a new round")
        print("2. End current round")
        print("3. Display rounds")
        print("4. Back to main menu")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                self.round_controller.create_round()
            case "2":
                self.round_controller.end_round()
            case "3":
                self.round_controller.display_rounds()
            case "4":
                return
            case _:
                print("Invalid choice. Please try again.")

    def display_matches(self, matches):
        """Display all matches in a round."""
        if not matches:
            print("No matches were found for this round.")
            return

        print("\nMatch list:")
        for i, match in enumerate(matches):
            print(f"{i + 1}. {match['player1']} vs {match['player2']} | Scores: {match['score1']} - {match['score2']}")

