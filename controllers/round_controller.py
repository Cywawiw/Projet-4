from models.round import Round
from models.player import Player
from controllers.match_controller import MatchController
from random import shuffle
from datetime import datetime
from models.match import Match


class RoundController:
    """
    Controller to manage round-related operations.
    """
    def __init__(self, tournament_controller):
        self.tournament_controller = tournament_controller
        self.tournament = None

    def set_tournament(self, tournament):
        """Set the current tournament."""
        self.tournament = tournament

    def create_round(self):
        """Create a new round for the selected tournament."""
        if not self.tournament:
            print("No tournament selected. Please select a tournament first.")
            return

        # Check if the maximum number of rounds is reached
        if len(self.tournament.rounds) >= self.tournament.num_rounds:
            print(f"Maximum number of rounds ({self.tournament.num_rounds}) reached for this tournament.")
            return

        round_number = len(self.tournament.rounds) + 1
        round_name = f"Round {round_number}"
        print(f"Creating {round_name} for '{self.tournament.name}'...")

        # Generate pairings
        matches = self.generate_pairings()
        if not matches:
            print("No matches could be created. Check the tournament data.")
            return

        # Create and add the round
        new_round = Round(
            name=round_name,
            matches=matches,
            start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.tournament.rounds.append(new_round)
        print(f"{round_name} created successfully.")

        # Save the tournament immediately to persist the round
        self.tournament_controller.save_tournament(self.tournament)
        print(f"{round_name} saved to the tournament.")

    def generate_pairings(self):
        """Generate player pairings for the current round."""
        players = [
            Player.from_dict(player) if isinstance(player, dict) else player
            for player in self.tournament.players
        ]

        # Shuffle players for the first round; sort by score otherwise
        if not self.tournament.rounds:
            print("First round: Shuffling players randomly...")
            shuffle(players)
        else:
            print("Sorting players by their scores for pairings...")
            players.sort(key=lambda player: player.score, reverse=True)

        matches, used_players = [], set()
        previous_matches = {
            (match.player1, match.player2) for round_ in self.tournament.rounds for match in round_.matches
        }

        # Create matches
        for player1 in players:
            if player1 in used_players:
                continue
            for player2 in players:
                if player2 in used_players or player1 == player2:
                    continue
                if (player1, player2) not in previous_matches and (player2, player1) not in previous_matches:
                    matches.append(Match(player1, player2))
                    used_players.update([player1, player2])
                    break

        # Handle unmatched players
        unmatched = [p for p in players if p not in used_players]
        if unmatched:
            print("Applying fallback pairing for unmatched players...")
            while len(unmatched) > 1:
                matches.append(Match(unmatched.pop(0), unmatched.pop(0)))
            if unmatched:
                print(f"Unmatched player remains without a partner: {unmatched[0]}")

        return matches

    def end_round(self):
        """
        End the current round and update match scores.
        """
        if not self.tournament or not self.tournament.rounds:
            print("No rounds available to end.")
            return

        current_round = self.tournament.rounds[-1]
        print(f"Ending the round '{current_round.name}'...")

        # Update scores for the current round
        match_controller = MatchController(current_round)  # Remove match_menu if unused
        match_controller.update_scores()

        # Mark the round as completed
        current_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Round '{current_round.name}' ended and scores updated.")

        # Save the tournament with updated round data
        self.tournament_controller.save_tournament(self.tournament)

    def display_rounds(self):
        """Display all rounds and their matches for the selected tournament."""
        if not self.tournament or not self.tournament.rounds:
            print("No rounds available for this tournament.")
            return

        print(f"Rounds in tournament '{self.tournament.name}':")
        for round_ in self.tournament.rounds:
            print(f"- {round_.name} (Start: {round_.start_time or 'Unknown'}, End: {round_.end_time or 'Ongoing'})")
            for match in round_.matches:
                # Ensure player1 is a Player instance
                player1 = match.player1 if isinstance(match.player1, Player) else Player.from_dict(match.player1)

                # Handle None for player2
                if match.player2 is None:
                    print(f"  Match: {player1} vs [No Opponent] | Scores: {match.score1} - {match.score2}")
                else:
                    player2 = match.player2 if isinstance(match.player2, Player) else Player.from_dict(match.player2)
                    print(f"  Match: {player1} vs {player2} | Scores: {match.score1} - {match.score2}")
