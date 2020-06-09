####
import sys
import pygame
import random as rand
from game.model.puck import Puck
from game.model.paddle import Paddle
from game.config.constants import *
from game.controllers.keyboard import NotifyRoundChange
####
class Event(object):
    """Uma classe que descreve os eventos em alto nível
    """
    def __init__(self)->None:
        self.name = "Generic Event"

    def __str__(self)->None:
        return self.name


class QuitEvent(Event):
    """ Sair do jogo
    """
    def __init__(self)->None:
        self.name = "Quit Event"


class TickEvent(Event):
    """Evento regular
    """
    def __init__(self)->None:
        self.name = "Tick Event"


class InputEvent(Event):
    """ Evento de input, por meio do mouse ou teclado
    """
    def __init__(self, unicode_char, click_position)->None:
        self.name = "Input Event"
        self.char = unicode_char
        self.click_position = click_position

    def __str__(self)->None:
        return f"{self.name}, char={self.char}, clickpos={self.click_position}"


class InitializeEvent(Event):
    """ Inicializa tudo
    """
    def __init__(self)->None:
        self.name = "Init Event"



class ChangeStateEvent(Event):
    """ Inicializa tudo
    """
    def __init__(self,state)->None:
        self.name = "Change State Event"
        self.state = state

####################
class Goal(Event):
    """ Retorna true if puck estiver dentro do gol
    """
    def __init__(self)->None:
        self.name = "Goal Event"

    def check_goal(self,side,puck):
        if side == LEFT:
            return (puck.x - puck.radius <= 0) and (puck.y >= GOAL_Y_LEFT) and (puck.y <= GOAL_Y_RIGHT)

        if side == RIGHT:
            return (puck.x + puck.radius >= WIDTH) and (puck.y >= GOAL_Y_LEFT) and (puck.y <= GOAL_Y_RIGHT)
    

class ResetGame(Event):
    def __init__(self)->None:
        self.name = "Reset Game"
    
    def reset_conditions(self,puck, paddle1, paddle2,speed, player,option):
        puck.reset(speed, player,option)
        paddle1.reset(22, HEIGHT / 2)
        paddle2.reset(WIDTH - 20, HEIGHT / 2)



class RoundChange(TickEvent):
    def __init__(self)->None:
        self.name = "Round Change"
        
        
    def notify_round_change(self, round_no,score1,score2)->None:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        small_font = pygame.font.SysFont("comicsans", 35)
        round_font = pygame.font.SysFont("comicsans", 45)
        clock = pygame.time.Clock()

        while True:
            NotifyRoundChange.notify(self)
            round_text = round_font.render("ROUND {0} COMPLETE".format(round_no), True, COLORS[2][0])
            screen.blit(round_text, [WIDTH / 2 - 150, HEIGHT / 2 - 50])

            score_text = round_font.render("{0}  :  {1}".format(score1, score2), True, BLACK)
            screen.blit(score_text, [WIDTH / 2 - 37, HEIGHT / 2])

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # continue
            x, y = WIDTH / 2 - 65, HEIGHT / 2 + 100
            if (mouse[0] > x) and (mouse[0] < x + 150) and (mouse[1] > y) and (mouse[1] < y + 40):
                pygame.draw.rect(screen, COLORS[4][1], (x, y, 150, 40))
                if click[0] == 1:
                    return
            else:
                pygame.draw.rect(screen, COLORS[4][0], (x, y, 150, 40))
            cont_text = small_font.render("CONTINUE", True, WHITE)
            screen.blit(cont_text, [x + 10, y + 10])

            text = small_font.render("OR", True, BLACK)
            screen.blit(text, [WIDTH / 2 - 18, HEIGHT - 150])
            text = small_font.render("press space to continue", True, BLACK)
            screen.blit(text, [WIDTH / 2 - 120, HEIGHT - 110])

            pygame.display.flip()
            clock.tick(10)

class EndGame(QuitEvent):
    def __int__(self)->None:
        self.name = "End Game"
    
    def game_end(self,screen, player):
        #Terminar de implementar
        return 1


    def end(self,puck,state,round,placar,speed,option)->None:
        # reset game with everything else same
        if option == 1:
            ResetGame.reset_conditions(self,puck,placar.paddle_left,placar.paddle_right,speed,1,1)
            ResetGame.reset_conditions(self,puck,placar.paddle_left,placar.paddle_right,speed,2,1)
            placar.score1, placar.score2 = 0, 0
            round.round_p1, round.round_p2 = 0, 0
            round.round_no = 1
            return False  # Tells that game should continue with reset

        # goes to menu
        elif option == 2:
            return True  # Game should restart at Start Screen

        # Quit game
        else:
            sys.exit()

###########################