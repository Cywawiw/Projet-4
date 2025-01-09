from datetime import datetime
from models.match import Match

class Round:
    """
    Model to represent a round within a tournament.
    """
    def __init__(self, name, matches, start_time=None, end_time=None):
        self.name = name
        self.matches = matches if matches is not None else []
        self.start_time = start_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = end_time

    def to_dict(self):
        """Convert the round object to a dictionary."""
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    @staticmethod
    def from_dict(data):
        """Create a round object from a dictionary."""
        matches = [Match.from_dict(m) for m in data["matches"]]
        return Round(
            name=data["name"],
            matches=matches,
            start_time=data["start_time"],
            end_time=data["end_time"],
        )