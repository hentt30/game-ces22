from game.subscriber.events import *
from game.model.paddle import Paddle
from game.config.constants import *
import pygame

class State(object):
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y, RIGHT)
        self.paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y, LEFT)

    def get_state(self) -> None:
        state = {
            "paddle_right": self.paddle_right.get_pos(),
            "paddle_left": self.paddle_left.get_pos()
        }
        return state

    def update(self) -> None:
        """ Muda o estado do jogo e avisa a tela
        """
        self.paddle_left.update()
        self.paddle_right.update()
        self.event_manager.post(ChangeStateEvent(self.get_state()))

#####################
class Placar:
    def __init__(self, event_manager) ->None:
        self.event_manager = event_manager
        self.score1=0
        self.score2=0

    def get_placar(self,screen)->None:
        """ Define a forma do placar e aciona na tela"""
        small_font = pygame.font.SysFont("comicsans", 35)
        text1 = small_font.render("{0} : {1}".format("Player 1", str(self.score1)), True, BLACK)
        text2 = small_font.render("{0} : {1}".format("Player 2", str(self.score2)), True, BLACK)

        screen.blit(text1, [40, 0])
        screen.blit(text2, [WIDTH - 150, 0])

    def update_placar(self, speed, puck,paddle1,paddle2)->None:
        """ Verifica o retorno de check_goal e atualiza o placar"""
        # Hits the left goal!
        if Goal.check_goal(self,LEFT,puck):
            self.score2 += 1
            ResetGame.reset_conditions(self,puck,paddle1,paddle2,speed, 1,1)
        # Hits the left goal!
        if Goal.check_goal(self,RIGHT,puck):
            self.score1 += 1
            ResetGame.reset_conditions(self,puck,paddle1,paddle2,speed, 2,1)


class Round:
    def __init__(self,event_manager)->None:
        self.event_manager=event_manager
        self.round_no=1
        self.round_p1=0
        self.round_p2=0

 
    def print_text(self,screen, text, center, font, color):
        """ Definir posição e formato do texto pro round """
        text_surf= font.render(text, True, color)
        text_rect= text_surf.get_rect()
        text_rect.center = center
        screen.blit(text_surf, text_rect)

    def get_round(self,screen):
        """ Define o round do jogo """
        round_font = pygame.font.SysFont("comicsans", 45)
        self.print_text(screen, "Round "+str(self.round_no), (WIDTH/2, 20), round_font, BLACK)
        self.print_text(screen, str(self.round_p1) + " : " + str(self.round_p2), (WIDTH / 2, 50), round_font, BLACK)

    def update_round(self,puck,paddle1,paddle2,score1,score2)->None:
        """ Verifica as condições necessárias e atualiza o round do jogo"""
        if score1 == SCORE_LIMIT:
            if not self.round_p1 + 1 == ROUND_LIMIT:
                RoundChange.notify_round_change(self, self.round_no, score1, score2)
            self.round_no += 1
            self.round_p1 += 1
            score1, score2 = 0, 0
            ResetGame.reset_conditions(self,puck,paddle1,paddle2,0,1,2)

        if score2 == SCORE_LIMIT:
            if not self.round_p2 + 1 == ROUND_LIMIT:
                RoundChange.notify_round_change(self, self.round_no, score1, score2)
            self.round_no += 1
            self.round_p2 += 1
            score1, score2 = 0, 0
            ResetGame.reset_conditions(self,puck,paddle1,paddle2,0,2,2)


###################