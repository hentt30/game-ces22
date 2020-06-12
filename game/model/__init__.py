from game.model.game import GameEngine
from game.model.state import State
from game.subscriber.__init__ import event_manager

game_engine = GameEngine(event_manager)
state = State(event_manager)
