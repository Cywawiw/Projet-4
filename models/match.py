from models.player import Player


class Match:
    """
    Model to represent a match between two players.
    """

    def __init__(self, player1, player2, score1=0.0, score2=0.0):
        """
        Initialize a Match object.

        Args:
            player1 (Player): The first player in the match.
            player2 (Player): The second player in the match. Can be None for odd players.
            score1 (float): Score of the first player. Defaults to 0.0.
            score2 (float): Score of the second player. Defaults to 0.0.
        """
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """
        Convert the Match object to a dictionary.

        Returns:
            dict: Dictionary representation of the match.
        """
        return {
            "player1": self.player1.to_dict() if self.player1 else None,
            "player2": self.player2.to_dict() if self.player2 else None,
            "score1": self.score1,
            "score2": self.score2
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Match object from a dictionary.

        Args:
            data (dict): Dictionary containing match data.

        Returns:
            Match: A Match object initialized from the dictionary.
        """
        return Match(
            player1=Player.from_dict(data["player1"]) if data["player1"] else None,
            player2=Player.from_dict(data["player2"]) if data["player2"] else None,
            score1=data["score1"],
            score2=data["score2"]
        )
