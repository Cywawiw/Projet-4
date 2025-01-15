from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController
from views.player_menu import PlayerMenu
from views.tournament_menu import TournamentMenu
from views.round_menu import RoundMenu
from views.main_menu import MainMenu

if __name__ == "__main__":
    player_controller = PlayerController()
    tournament_controller = TournamentController(player_controller)
    round_menu = RoundMenu(None)
    round_controller = RoundController(tournament_controller, round_menu)
    round_menu.round_controller = round_controller
    match_controller = MatchController(None, None)

    player_menu = PlayerMenu(player_controller)
    round_menu = RoundMenu(round_controller)
    tournament_menu = TournamentMenu(tournament_controller, round_controller)

    main_menu = MainMenu(player_menu, tournament_menu, round_menu)
    main_menu.display_menu()


