class MatchController:
    """
    Controller to manage matches in a round.
    """
    def __init__(self, round_, match_menu):
        self.round = round_
        self.match_menu = match_menu

    def display_matches(self):
        """Display all matches."""
        self.match_menu.display_matches(self.round.matches)

    def update_scores(self):
        """Prompt the user to update scores for matches in the round."""
        print("\nUpdating scores for the current round...")
        for match in self.round.matches:
            if not match.player2:
                print(f"{match.player1} has no opponent in this match.")
                continue

            print(f"Match: {match.player1} vs {match.player2}")
            while True:  # Repeat until valid scores are entered
                try:
                    score1 = float(input(f"Enter the score for {match.player1} (0, 0.5, or 1): "))
                    score2 = float(input(f"Enter the score for {match.player2} (0, 0.5, or 1): "))

                    # Validate that the total score is 1
                    if score1 + score2 == 1 and score1 in [0, 0.5, 1] and score2 in [0, 0.5, 1]:
                        match.score1 = score1
                        match.score2 = score2
                        print(f"Scores updated: {match.player1} ({score1}) - {match.player2} ({score2})")
                        break  # Exit the loop if scores are valid
                    else:
                        print("Invalid scores. The total score must equal 1. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter numeric values (0, 0.5, or 1).")