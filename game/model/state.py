from game.subscriber.events import *
from game.model.paddle import Paddle
from game.model.puck import Puck
from game.config.constants import *
#from game.view.__init__ import game_view
import pygame

global score1, score2
class State(object):
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y, RIGHT)
        self.paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y, LEFT)
        self.puck = Puck()
        self.placar= Placar(event_manager,0,0)
        self.round= Round(event_manager,1,0,0)

    def get_state(self) -> None:
        state = {
            "paddle_right": self.paddle_right.get_pos(),
            "paddle_left": self.paddle_left.get_pos(),
            "puck": self.puck.get_pos(),
            "placar": self.placar.get_placar(),
            "round": self.round.get_round()
        }
        return state

    def update(self) -> None:
        """ Muda o estado do jogo e avisa a tela
        """
        self.paddle_left.update()
        self.paddle_right.update()
        self.puck.update(self.paddle_left, self.paddle_right)
        self.placar.update_placar(0,self)
        self.round.update_round(0,self)
        self.event_manager.post(ChangeStateEvent(self.get_state()))

#####################
class Placar:
    def __init__(self, event_manager, score1,score2) ->None:
        self.event_manager = event_manager
        self.score1=score1
        self.score2=score2
        self.screen= pygame.display.set_mode((WIDTH, HEIGHT))

    def render_placar(self)->None:
        """ Define a forma do placar e aciona na tela"""
        small_font = pygame.font.SysFont("comicsans", 35)
        text1 = small_font.render("{0} : {1}".format("Player 1",str(self.score1)), True, BLACK)
        text2 = small_font.render("{0} : {1}".format("Player 2", str(self.score2)), True, BLACK)
    
        self.screen.blit(text1, [40, 0])
        self.screen.blit(text2, [WIDTH - 150, 0])
        pygame.display.flip()

    def get_placar(self):   
        return self.score1, self.score2

    def render_update_placar(self,scores):
        self.score1= scores[0]
        self.score2= scores[1]

    def update_placar(self, speed,state)->None:
        """ Verifica o retorno de check_goal e atualiza o placar"""
        if state is not None:
            # Hits the left goal!
            if Goal.check_goal(self,LEFT,state.puck):
                self.score2 += 1
                ResetGame.reset_conditions(self,state.puck,state.paddle_left,
                state.paddle_right,speed, 2,2)
            # Hits the left goal!
            if Goal.check_goal(self,RIGHT,state.puck):
                self.score1 += 1
                ResetGame.reset_conditions(self,state.puck,state.paddle_left,
                state.paddle_right,speed, 1,2)


class Round:
    def __init__(self,event_manager, round_no,round_p1, round_p2)->None:
        self.event_manager=event_manager
        self.round_no= round_no
        self.round_p1= round_p1
        self.round_p2= round_p2
        self.screen= pygame.display.set_mode((WIDTH, HEIGHT))

 
    def render_round(self):
        """ Imprime  o round do jogo """
        round_font = pygame.font.SysFont("comicsans", 45)
        EndGame.print_text(self, self.screen, "Round "+str(self.round_no), (WIDTH/2, 20), round_font, BLACK)
        EndGame.print_text(self ,self.screen, str(self.round_p1) + " : " + str(self.round_p2), (WIDTH / 2, 50), round_font, BLACK)

    def get_round(self):
        return self.round_no, self.round_p1, self.round_p2

    def render_update_round(self,rounds):
        self.round_no= rounds[0]
        self.round_p1= rounds[1]
        self.round_p2= rounds[2]
    
    def update_round(self,speed,state)->None:
        """ Verifica as condições necessárias e atualiza o round do jogo"""
        if state is not None:
            if state.placar.score1 == SCORE_LIMIT:
                if not self.round_p1 + 1 == ROUND_LIMIT:
                    RoundChange.notify_round_change(self, self.round_no, state.placar.score1, state.placar.score2)
                self.round_no += 1
                self.round_p1 += 1
                state.placar.score1, state.placar.score2 = 0, 0
                ResetGame.reset_conditions(self,state.puck,state.paddle_left,state.paddle_right,0,1,1)

            if state.placar.score2 == SCORE_LIMIT:
                if not self.round_p2 + 1 == ROUND_LIMIT:
                    RoundChange.notify_round_change(self,self.round_no, state.placar.score1,state.placar.score2)
                self.round_no += 1
                self.round_p2 += 1
                state.placar.score1, state.placar.score2 = 0, 0
                ResetGame.reset_conditions(self,state.puck,state.paddle_left,
                state.paddle_right,0,2,1)

            if self.round_p1 == ROUND_LIMIT:  # Player one denotes left player
                self.get_winner(1,state.puck,self.screen,speed)
            if self.round_p2 == ROUND_LIMIT:  # Player two denotes right player
                self.get_winner(2,state.puck,self.screen,speed)

    def  get_winner(self,player,puck,screen,speed)->None:
        """ Define o vencedor """
        state = EndGame()
        if EndGame.end(self,puck, State, Round, Placar, speed, state.game_end(screen,player)):
            #Modifica musica aqui
            return
        else:
            self.render_round()


###################