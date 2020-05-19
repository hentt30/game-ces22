from game.view.pygame_view import PyGameView
from game.controllers.keyboard import Keyboard
from game.model.game import GameEngine
from game.subscriber.event_manager import EventManager
###
from game.model.puck import *
from game.config.constants import*
from game.model.state import*


puck = Puck(WIDTH / 2, HEIGHT / 2)
paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y,0)
paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y,1)

small_font = pygame.font.SysFont("comicsans", 35)
round_font = pygame.font.SysFont("comicsans", 45)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
score1= 0 
score2= 0

def text_obj(text, font, color):
    """ Define o objeto de texto"""
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()
 
def disp_text(screen, text, center, font_and_size, color):
    """ Exibe texto """
    text_surf, text_rect = text_obj(text, font_and_size, color)
    text_rect.center = center
    screen.blit(text_surf, text_rect)

def get_placar(self):
    """ Define o placar do jogo""" 
    text1 = small_font.render("{0} : {1}".format("Player 1", str(score1)), True, BLACK)
    text2 = small_font.render("{0} : {1}".format("Player 2", str(score2)), True, BLACK)

    screen.blit(text1, [40, 0])
    screen.blit(text2, [WIDTH - 150, 0])

def get_round(rounds_p1, rounds_p2, round_no):
    """ Define o round do jogo """
    disp_text(screen, "Round "+str(round_no), (WIDTH/2, 20), round_font, BLACK)
    disp_text(screen, str(rounds_p1) + " : " + str(rounds_p2), (WIDTH / 2, 50), round_font, BLACK)

def check_goal(side):
    """ Retorna true if puck estiver dentro do gol"""
    if side == LEFT:
        return (puck.x - puck.radius <= 0) and (puck.y >= GOAL_Y_LEFT) and (puck.y <= GOAL_Y_RIGHT)

    if side == RIGHT:
        return (puck.x + puck.radius >= WIDTH) and (puck.y >= GOAL_Y_LEFT) and (puck.y <= GOAL_Y_RIGHT)

def reset_game_round(speed, player,option):
    """ Retorna os objetos e round para as codições padrão """
    puck.reset(speed, player, option)
    paddle_left.reset(22, HEIGHT / 2)
    paddle_right.reset(WIDTH - 20, HEIGHT / 2)

###

def main() -> None:
    event_manager = EventManager()

    game_engine = GameEngine(event_manager)
    keyboard = Keyboard(event_manager)
    game_view = PyGameView(event_manager)

    game_engine.run()


if __name__ == "__main__":
    main()
