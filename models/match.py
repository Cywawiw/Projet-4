class Match:
    """
    Model to represent a match between two players.
    """
    def __init__(self, player1, player2, score1=0.0, score2=0.0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Convert the match object to a dictionary."""
        return {
            "player1": self.player1,
            "player2": self.player2,
            "score1": self.score1,
            "score2": self.score2
        }

    @staticmethod
    def from_dict(data):
        """Create a match object from a dictionary."""
        return Match(
            player1=data["player1"],
            player2=data["player2"],
            score1=data["score1"],
            score2=data["score2"]
        )