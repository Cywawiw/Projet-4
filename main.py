from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController
from controllers.report_controller import ReportController
from views.player_menu import PlayerMenu
from views.tournament_menu import TournamentMenu
from views.main_menu import MainMenu
from views.report_menu import ReportMenu

if __name__ == "__main__":
    """
    Main execution block of the application.
    Initializes all controllers and menus, and starts the main menu loop.
    """
    player_controller = PlayerController()
    tournament_controller = TournamentController(player_controller)
    round_controller = RoundController(tournament_controller)
    match_controller = MatchController(None)
    report_controller = ReportController(player_controller, tournament_controller)

    player_menu = PlayerMenu(player_controller)
    tournament_menu = TournamentMenu(tournament_controller, round_controller)
    report_menu = ReportMenu(report_controller)

    main_menu = MainMenu(player_menu, tournament_menu, report_menu)
    main_menu.display_menu()
