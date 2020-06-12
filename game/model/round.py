from game.config.constants import *
from game.subscriber.events import *
import pygame

class Round:
    def __init__(self,event_manager)->None:
        self.event_manager = event_manager
        self.round_no = 1
        self.round_p1 = 0
        self.round_p2 = 0

    def get_round(self):
        return self.round_no, self.round_p1, self.round_p2

    def set_round(self,rounds):
        self.round_no = rounds[0]
        self.round_p1 = rounds[1]
        self.round_p2 = rounds[2]
    
    def update(self,state)->None:
        """ Verifica as condições necessárias e atualiza o round do jogo"""
        if state is not None:
            round_change = RoundChange()
            reset = ResetGame()
            if state.placar.score1 == SCORE_LIMIT:
                if not self.round_p1 + 1 == ROUND_LIMIT:
                    round_change.notify_round_change(self.round_no, state.placar.score1, state.placar.score2)
                self.round_no += 1
                self.round_p1 += 1
                state.placar.score1, state.placar.score2 = 0, 0
                reset.reset_conditions(state.puck,state.paddle_left,state.paddle_right,1,1)

            if state.placar.score2 == SCORE_LIMIT:
                if not self.round_p2 + 1 == ROUND_LIMIT:
                    round_change.notify_round_change(self.round_no, state.placar.score1,state.placar.score2)
                self.round_no += 1
                self.round_p2 += 1
                state.placar.score1, state.placar.score2 = 0, 0
                reset.reset_conditions(state.puck,state.paddle_left, state.paddle_right,2,1)

            if self.round_p1 == ROUND_LIMIT:  # Player one denotes left player
                self.get_winner(1,state)
            if self.round_p2 == ROUND_LIMIT:  # Player two denotes right player
                self.get_winner(2,state)

    def get_winner(self,player,state)->None:
        """ Define o vencedor """
        event = EndGame()
        if event.end(state, event.game_end(player)):
            #Modifica musica aqui
            return
        else:
            self.event_manager.post(InitializeEvent())
