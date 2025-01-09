from controllers.match_controller import MatchController
from views.main_menu import MainMenu
from views.player_menu import PlayerMenu
from views.tournament_menu import TournamentMenu
from views.round_menu import RoundMenu
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController

if __name__ == "__main__":
    # Initialisation des contrôleurs
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    round_controller = RoundController(None, None)
    match_controller = MatchController(None,None)

    # Initialisation des menus
    player_menu = PlayerMenu(player_controller)
    round_menu = RoundMenu(round_controller)
    tournament_menu = TournamentMenu(tournament_controller, round_controller)

    # Initialisation du menu principal
    main_menu = MainMenu(player_menu, tournament_menu, round_menu)
    main_menu.display_menu()
