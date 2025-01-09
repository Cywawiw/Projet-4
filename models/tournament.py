from models.round import Round

class Tournament:
    """
    Model to represent a chess tournament.
    """
    def __init__(self, name, location, start_date, end_date, description, 
                 num_rounds=4, current_round=0, rounds=None, players=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []

    def to_dict(self):
        """Convert the tournament object to a dictionary."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "players": self.players
        }

    @staticmethod
    def from_dict(data):
        """Create a tournament object from a dictionary."""
        return Tournament(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            num_rounds=data.get("num_rounds", 4),
            current_round=data.get("current_round", 0),
            rounds=[Round.from_dict(r) for r in data.get("rounds", [])],
            players=data.get("players", [])
        )