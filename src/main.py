from controller.game_controller import GameController
from src.model.turn import TurnSetUp


def main():
    game_controller = GameController()
    game_controller.begin_game()


if __name__ == "__main__":
    the_set_up = TurnSetUp()
    the_turn = the_set_up.get_turn_flow()

    wait_for_input = the_turn.handle_request()

    while True:
        if not wait_for_input:
            wait_for_input = the_turn.handle_request()



    #main()
