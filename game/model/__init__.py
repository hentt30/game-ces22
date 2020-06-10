from game.model.game import GameEngine
from game.model.paddle import Paddle
from game.model.puck import Puck
from game.model.state import *
from game.model.utils import *
from game.config.constants import*
from game.subscriber.__init__ import event_manager

#Inicializar 
puck = Puck(WIDTH / 2, HEIGHT / 2)
paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y,0)
paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y,1)

state= State(event_manager)
placar = Placar(event_manager)
round= Round(event_manager)



