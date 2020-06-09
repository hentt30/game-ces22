from game.view.pygame_view import PyGameView
from game.controllers.keyboard import Keyboard
from game.model.game import GameEngine
from game.subscriber.event_manager import EventManager
from game.model.puck import Puck
from game.config.constants import*
from game.model.state import*


puck = Puck(WIDTH / 2, HEIGHT / 2)
paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y,0)
paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y,1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))



def main() -> None:
    event_manager = EventManager()

    game_engine = GameEngine(event_manager)
    keyboard = Keyboard(event_manager)
    game_view = PyGameView(event_manager)

    game_engine.run()


if __name__ == "__main__":
    main()
