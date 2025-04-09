from models.round import Round
from models.player import Player


class Tournament:
    """
    Model to represent a chess tournament.
    """

    def __init__(self, name, location, start_date, end_date, description, num_rounds=4,
                 players=None, rounds=None, current_round=0):
        """
        Initialize a Tournament object.

        Args:
            name (str): Name of the tournament.
            location (str): Location of the tournament.
            start_date (str): Start date in DD-MM-YYYY format.
            end_date (str): End date in DD-MM-YYYY format.
            description (str): Description or notes about the tournament.
            num_rounds (int): Number of rounds in the tournament. Defaults to 4.
            players (list): List of Player objects participating. Defaults to an empty list.
            rounds (list): List of Round objects in the tournament. Defaults to an empty list.
            current_round (int): Current round number. Defaults to 0.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.players = players or []
        self.rounds = rounds or []
        self.current_round = current_round

    def to_dict(self):
        """
        Convert the Tournament object to a dictionary.

        Returns:
            dict: Dictionary representation of the tournament.
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "num_rounds": self.num_rounds,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "current_round": self.current_round
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Tournament object from a dictionary.

        Args:
            data (dict): Dictionary containing tournament data.

        Returns:
            Tournament: A Tournament object initialized from the dictionary.
        """
        return Tournament(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            num_rounds=data["num_rounds"],
            players=[Player.from_dict(p) for p in data["players"]],
            rounds=[Round.from_dict(r) for r in data.get("rounds", [])],
            description=data["description"]
        )
