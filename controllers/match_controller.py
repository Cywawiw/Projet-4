class MatchController:
    """
    Controller for managing match operations within a round.
    """
    def __init__(self, current_round):
        """
        Initialize the MatchController with the current round.

        Args:
            current_round (Round): The round containing the matches.
        """
        self.current_round = current_round

    def update_scores(self):
        """
        Update scores for each match in the current round.
        """
        for match in self.current_round.matches:
            if match.player1 and match.player2:
                print(f"Match: {match.player1} vs {match.player2}")

                # Input scores for each player
                try:
                    score1 = float(input(f"Enter the score for {match.player1} (0, 0.5, or 1): ").strip())
                    score2 = float(input(f"Enter the score for {match.player2} (0, 0.5, or 1): ").strip())
                except ValueError:
                    print("Invalid input. Please enter 0, 0.5, or 1.")
                    continue

                # Validate total match score
                if score1 + score2 != 1.0:
                    print("Invalid match score: Total must equal 1.0. Try again.")
                    continue

                # Assign scores to the match
                match.score1 = score1
                match.score2 = score2

                # Update players' scores
                match.player1.score += score1
                match.player2.score += score2

                print(
                    f"Scores updated:"
                    f" {match.player1} ({match.player1.score}) - {match.player2} ({match.player2.score})")
            else:
                print("Skipping match with missing player.")
