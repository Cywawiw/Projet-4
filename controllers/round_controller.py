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
    def __init__(self, tournament_controller, round_menu):
        self.tournament_controller = tournament_controller
        self.round_menu = round_menu  # Associer round_menu
        self.tournament = None  # Initialiser comme None

    def set_tournament(self, tournament):
        """Set the current tournament."""
        self.tournament = tournament

    def create_round(self):
        """Create a new round for the selected tournament."""
        if not self.tournament:
            print("No tournament selected. Please select a tournament first.")
            return

        # Vérifiez si le nombre maximal de rondes est atteint
        if len(self.tournament.rounds) >= self.tournament.num_rounds:
            print(f"Maximum number of rounds ({self.tournament.num_rounds}) reached for this tournament.")
            return

        round_number = len(self.tournament.rounds) + 1
        round_name = f"Round {round_number}"

        print(f"Creating {round_name} for '{self.tournament.name}'...")

        # Générer les appariements
        matches = self.generate_pairings()
        if not matches:
            print("No matches could be created. Check the tournament data.")
            return

        # Créer et ajouter la ronde
        new_round = Round(name=round_name, matches=matches)
        self.tournament.rounds.append(new_round)
        print(f"{round_name} created successfully.")

        # Sauvegarder le tournoi via TournamentController
        self.tournament_controller.save_tournament(self.tournament)


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
            print("No rounds available to end.")
            return

        current_round = self.tournament.rounds[-1]
        print(f"Ending the round '{current_round.name}'...")

        # Demander les scores des matchs
        match_controller = MatchController(current_round, self.round_menu)
        match_controller.update_scores()

        # Marquer la ronde comme terminée
        current_round.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Round '{current_round.name}' ended and scores updated.")

        # Sauvegarder le tournoi
        self.tournament_controller.save_tournament(self.tournament)

    def display_rounds(self):
        """Display all rounds and their matches for the selected tournament."""
        if not self.tournament or not self.tournament.rounds:
            print("No rounds available for this tournament.")
            return

        print(f"Rounds in tournament '{self.tournament.name}':")
        for round_ in self.tournament.rounds:
            print(f"- {round_.name} (Start: {round_.start_time}, End: {round_.end_time or 'Ongoing'})")
            for match in round_.matches:
                player1 = match.player1 if isinstance(match.player1, Player) else Player.from_dict(match.player1)
                player2 = match.player2 if isinstance(match.player2, Player) else Player.from_dict(match.player2)
                print(f"  Match: {player1} vs {player2} | Scores: {match.score1} - {match.score2}")

        print(f"Rounds in tournament '{self.tournament.name}':")
        for round_ in self.tournament.rounds:
            print(f"- {round_.name} (Start: {round_.start_time}, End: {round_.end_time or 'Ongoing'})")
            for match in round_.matches:
                print(f"  Match: {match.player1} vs {match.player2} | Scores: {match.score1} - {match.score2}")
