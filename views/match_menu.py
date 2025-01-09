class MatchMenu:
    """
    View to display the match menu and handle user interactions.
    """
    def display_menu(self):
        """Display the match menu options."""
        print("\nMatch Menu")
        print("1. Display matches")
        print("2. Update match scores")
        print("3. Back to main menu")
        choice = input("Choose an option: ")


    def display_matches(self, matches):
        """Display all matches in a round."""
        if not matches:
            print("No matches were found for this round.")
            return

        print("\nMatch list :")
        for i, match in enumerate(matches):
            print(f"{i + 1}. {match.player1} vs {match.player2} | Scores : {match.score1} - {match.score2}")

    def prompt_round_selection(self, rounds):
        """Prompt the user to select a round."""
        print("\nrounds available :")
        for i, round_ in enumerate(rounds):
            print(f"{i + 1}. {round_.name}")
        return input("Select a round by number : ")

    def prompt_score_update(self, match):
        """Prompt the user to update the scores for a match."""
        print(f"\nUpdating scores for the match : {match.player1} vs {match.player2}")
        score1 = input(f"Select score for {match.player1} : ")
        score2 = input(f"Select score for {match.player2} : ")
        return score1, score2
