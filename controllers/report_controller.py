class ReportController:
    """
    Controller to generate and display reports.
    """
    def __init__(self, player_controller, tournament_controller):
        self.player_controller = player_controller
        self.tournament_controller = tournament_controller

    def list_players(self):
        """Display a list of all players sorted alphabetically."""
        players = self.player_controller.load_players()
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        print("\nList of all players (alphabetical):")
        for player in sorted_players:
            print(player)

    def list_tournaments(self):
        """Display a list of all tournaments."""
        tournaments = self.tournament_controller.load_tournaments()
        print("\nList of all tournaments:")
        for tournament in tournaments:
            print(f"{tournament.name} ({tournament.start_date} - {tournament.end_date})")

    def tournament_details(self, tournament_name):
        """Display the name and dates of a given tournament."""
        tournament = self._get_tournament_by_name(tournament_name)
        if tournament:
            print(f"\nTournament '{tournament.name}':")
            print(f"Location: {tournament.location}")
            print(f"Dates: {tournament.start_date} - {tournament.end_date}")
            print(f"Description: {tournament.description}")
        else:
            print(f"Tournament '{tournament_name}' not found.")

    def list_tournament_players(self, tournament_name):
        """Display a list of players in a given tournament sorted alphabetically."""
        tournament = self._get_tournament_by_name(tournament_name)
        if tournament:
            sorted_players = sorted(tournament.players, key=lambda p: (p.last_name, p.first_name))
            print(f"\nPlayers in tournament '{tournament.name}':")
            for player in sorted_players:
                print(player)
        else:
            print(f"Tournament '{tournament_name}' not found.")

    def list_tournament_rounds(self, tournament_name):
        """Display all rounds and matches of a given tournament."""
        tournament = self._get_tournament_by_name(tournament_name)
        if tournament:
            print(f"\nRounds in tournament '{tournament.name}':")
            for round_ in tournament.rounds:
                print(f"- {round_.name} (Start: {round_.start_time}, End: {round_.end_time or 'Ongoing'})")
                for match in round_.matches:
                    print(f"  Match: {match.player1} vs {match.player2} | Scores: {match.score1} - {match.score2}")
        else:
            print(f"Tournament '{tournament_name}' not found.")

    def _get_tournament_by_name(self, name):
        """Retrieve a tournament by its name."""
        tournaments = self.tournament_controller.load_tournaments()
        for tournament in tournaments:
            if tournament.name.lower() == name.lower():
                return tournament
        return None
