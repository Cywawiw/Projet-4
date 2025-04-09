from models.match import Match


class Round:
    """
    Model to represent a round within a tournament.
    """

    def __init__(self, name, matches, start_time=None, end_time=None):
        """
        Initialize a Round object.

        Args:
            name (str): The name of the round (e.g., "Round 1").
            matches (list): List of Match objects in the round.
            start_time (str): Start time of the round. Defaults to None.
            end_time (str): End time of the round. Defaults to None.
        """
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        """
        Convert the Round object to a dictionary.

        Returns:
            dict: Dictionary representation of the round.
        """
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Round object from a dictionary.

        Args:
            data (dict): Dictionary containing round data.

        Returns:
            Round: A Round object initialized from the dictionary.
        """
        return Round(
            name=data["name"],
            matches=[Match.from_dict(m) for m in data["matches"]],
            start_time=data.get("start_time"),
            end_time=data.get("end_time")
        )
