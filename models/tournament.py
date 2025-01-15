from models.round import Round
from models.player import Player

class Tournament:
    """
    Model to represent a chess tournament.
    """
    def __init__(self, name, location, start_date, end_date, description, num_rounds=4, players=None, rounds=None, current_round=0):
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
        """Convert the tournament object to a dictionary."""
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
        """Create a tournament object from a dictionary."""
        tournament = Tournament(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            num_rounds=data.get("num_rounds", 4),
            players=[Player.from_dict(p) for p in data.get("players", [])],
            rounds=[Round.from_dict(r) for r in data.get("rounds", [])],
            current_round=data.get("current_round", 0)
        )
        return tournament
