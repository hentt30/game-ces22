import sys
import pygame
import string
import random as rand
from game.model.puck import Puck
from game.model.paddle import Paddle
from game.config.constants import *

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
    
    def reset_conditions(self,puck, paddle1, paddle2, player,option):
        puck.reset(player,option)
        paddle1.reset(22, HEIGHT / 2)
        paddle2.reset(WIDTH - 20, HEIGHT / 2)


class RoundChange(TickEvent):
    def __init__(self)->None:
        self.name = "Round Change"

       
    def notify_round_change(self, round_no,score1,score2):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        small_font = pygame.font.SysFont("comicsans", 35)
        round_font = pygame.font.SysFont("comicsans", 45)
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            return
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
    
    def game_end(self, player):
        large_text = pygame.font.Font('freesansbold.ttf', 45)
        small_text = pygame.font.Font('freesansbold.ttf', 30)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        while True:
            # to smoothly shine winning message
            delay = 0
            screen.fill(BACKGROUND_COLOR)
            event = PressButton()
            event.get_input(TickEvent())
            color_x = rand.randint(0, 4)
            color_y = rand.randint(0, 1)
            # print which player won
            if delay == 0:        
                font = pygame.font.SysFont("comicsans", 45)
                text_surf = font.render("PLAYER {} WINS".format(player), True, COLORS[color_x][color_y])
                text_rect = text_surf.get_rect()
                text_rect.center = (WIDTH / 2, HEIGHT / 2 - 150)
                screen.blit(text_surf, text_rect)
            # drawing buttons for reset, menu and exit.
            event = PressButton()
            aux = event.draw_buttons(screen)
            if aux == 1 or aux == 2:
                return aux
            pygame.display.update()
            clock.tick(10)



    def end(self,state,option):
        # reset game with everything else same
        if option == 1:
            event= ResetGame()
            event.reset_conditions(state.puck,state.paddle_left,state.paddle_right,1,1)
            event.reset_conditions(state.puck,state.paddle_left,state.paddle_right,2,1)
            state.placar.score1, state.placar.score2 = 0, 0
            state.round.round_p1, state.round.round_p2 = 0, 0
            state.round.round_no = 1
            return False  # Tells that game should continue with reset

        # Quit game
        else:
            sys.exit()

class PressButton(InputEvent):
    """ Pressiona botão e exibe mensagem"""
    def __init__(self)->None:
        self.name = "Press Button"
        self.buttonRadius = 60
    
    def get_input(self,event):
        if (isinstance(event, TickEvent)):
            for event in pygame.event.get():
                # Press R to reset game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return 1
                # Press M to go to menu
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    return 2
                # Press esc or Q to quit
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
    def text_obj(self,text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def button_circle(self,screen, butt_color, button_pos, text, text_size, text_color,text_pos):
        pygame.draw.circle(screen, butt_color, button_pos, self.buttonRadius)
        text_surf, text_rect = self.text_obj(text, text_size, text_color)
        text_rect.center = text_pos
        screen.blit(text_surf, text_rect)

    def draw_buttons(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        large_text = pygame.font.Font('freesansbold.ttf', 45)
        small_text = pygame.font.Font('freesansbold.ttf', 30)

        # Reset button
        if abs(mouse_pos[0] - 200) < self.buttonRadius and abs(mouse_pos[1] - 470) < self.buttonRadius:
            self.button_circle(screen, COLORS[0][1], (200, 470), "Reset", large_text, (255, 255, 255),
                          (WIDTH / 2 - 400, HEIGHT / 2 + 170))
            if mouse_press[0] == 1:
                return 1

        else:
            self.button_circle(screen, COLORS[0][0], (200, 470), "Reset", small_text, (255, 255, 255),
                          (WIDTH / 2 - 400, HEIGHT / 2 + 170))


        # quit button
        if abs(mouse_pos[0] - 1000) < self.buttonRadius and abs(mouse_pos[1] - 470) < self.buttonRadius:
            self.button_circle(screen, COLORS[1][1], (1000, 470), "Quit", large_text, (255, 255, 255),
                          (WIDTH / 2 + 400, HEIGHT / 2 + 170))
            if mouse_press[0] == 1:
                return 2
                pygame.quit()        
                
        else:
            self.button_circle(screen, COLORS[1][0], (1000, 470), "Quit", small_text, (255, 255, 255),
                          (WIDTH / 2 + 400, HEIGHT / 2 + 170))
