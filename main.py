from game.view.pygame_view import PyGameView
from game.controllers.keyboard import Keyboard
from game.model.game import GameEngine
from game.subscriber.event_manager import EventManager


def main() -> None:
    event_manager = EventManager()

    game_engine = GameEngine(event_manager)
    keyboard = Keyboard(event_manager)
    game_view = PyGameView(event_manager)

    game_engine.run()


if __name__ == "__main__":
    main()
