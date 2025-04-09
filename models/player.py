class Player:
    """
    Model to represent a chess player.
    """

    def __init__(self, first_name, last_name, birth_date, chess_id, score=0.0):
        """
        Initialize a Player object.

        Args:
            first_name (str): The first name of the player.
            last_name (str): The last name of the player.
            birth_date (str): The player's date of birth in DD-MM-YYYY format.
            chess_id (str): The unique identifier for the player.
            score (float): The player's current score in the tournament. Defaults to 0.0.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def __str__(self):
        """
        String representation of the player.

        Returns:
            str: Player's name and ID in formatted text.
        """
        return f"{self.last_name}, {self.first_name} ({self.chess_id})"

    def to_dict(self):
        """
        Convert the Player object to a dictionary.

        Returns:
            dict: Dictionary representation of the player.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Player object from a dictionary.

        Args:
            data (dict): Dictionary containing player data.

        Returns:
            Player: A Player object initialized from the dictionary.
        """
        if not isinstance(data, dict):
            raise TypeError(f"Expected a dictionary, got {type(data).__name__}: {data}")
        return Player(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"],
            score=data.get("score", 0.0),
        )
