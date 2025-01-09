class Player:
    """
    Model to represent a chess player.
    """
    def __init__(self, first_name, last_name, birth_date, chess_id, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.chess_id})"

    def to_dict(self):
        """Convert the player object to a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score
        }

    @staticmethod
    def from_dict(data):
        """Create a player object from a dictionary."""
        if not isinstance(data, dict):
            raise TypeError(f"Expected a dictionary, got {type(data).__name__}: {data}")
        return Player(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            chess_id=data["chess_id"],
            score=data.get("score", 0),
        )