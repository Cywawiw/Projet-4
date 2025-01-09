from models.round import Round
from models.player import Player
from controllers.match_controller import MatchController
from random import shuffle
from datetime import datetime
from models.match import Match

class RoundController:
    """
    Controller to manage rounds and their operations.
    """
    def __init__(self, tournament, round_menu):
        self.tournament = tournament
        self.round_menu = round_menu

    def create_round(self):
        """Create a new round and save it to the tournament."""
        if not self.tournament:
            print("No tournament selected. Please select a tournament first.")
            return

        round_number = len(self.tournament.rounds) + 1
        round_name = f"Round {round_number}"
        print(f"Creating {round_name} for '{self.tournament.name}'...")

        # Generate player pairings
        matches = self.generate_pairings()

        # Create the new round
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_round = Round(name=round_name, matches=matches, start_time=start_time)

        # Save the round in the tournament
        self.tournament.rounds.append(new_round)
        print(f"Round '{round_name}' created successfully.")

    def generate_pairings(self):
        """Generate player pairings for the current round."""
        players = [
            Player.from_dict(player) if isinstance(player, dict) else player
            for player in self.tournament.players
        ]

        # First round: Random shuffle
        if len(self.tournament.rounds) == 0:
            print("First round: Shuffling players randomly...")
            shuffle(players)

        # Subsequent rounds: Sort players by score descending
        else:
            print("Sorting players by their scores for pairings...")
            try:
                players = sorted(players, key=lambda player: player.score, reverse=True)
            except AttributeError as e:
                print(f"Error sorting players: {e}")
                return []

        matches = []
        used_players = set()

        for i, player1 in enumerate(players):
            if player1 in used_players:
                continue

            for player2 in players[i + 1:]:
                if player2 in used_players:
                    continue

                previous_matches = {
                    (match.player1, match.player2) for round_ in self.tournament.rounds for match in round_.matches
                }
                if (player1, player2) not in previous_matches and (player2, player1) not in previous_matches:
                    matches.append(Match(player1, player2))
                    used_players.add(player1)
                    used_players.add(player2)
                    break

        # Handle odd players
        for player in players:
            if player not in used_players:
                matches.append(Match(player, None))
                break

        return matches

    def end_round(self):
        """End the current round and update match scores."""
        if not self.tournament or not self.tournament.rounds:
            print("No current round available to end.")
            return

        current_round = self.tournament.rounds[-1]
        if current_round.end_time:
            print(f"The round '{current_round.name}' has already been ended.")
            return

        print(f"Ending the round '{current_round.name}'...")
        match_controller = MatchController(current_round, self.round_menu)
        match_controller.update_scores()

        current_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Round '{current_round.name}' ended and scores updated.")

    def display_rounds(self):
        """Display all rounds in the selected tournament."""
        if not self.tournament or not self.tournament.rounds:
            print("No rounds available in this tournament.")
            return

        print(f"Rounds in tournament '{self.tournament.name}':")
        for round_ in self.tournament.rounds:
            print(f"- {round_.name} (Start: {round_.start_time}, End: {round_.end_time or 'Ongoing'})")
            for match in round_.matches:
                print(f"  Match: {match.player1} vs {match.player2} | Scores: {match.score1} - {match.score2}")
