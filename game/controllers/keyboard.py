import pygame
from game.subscriber.events import *


class Keyboard(object):
    """ Trata dos inputs do teclado
    """
    def __init__(self, event_manager) -> None:

        self.event_manager = event_manager
        self.event_manager.subscribe_listener(self)

    def notify(self, event) -> None:
        """ Notifica o teclado se o usuário pressionar alguma tecla
        """
        if (isinstance(event, TickEvent)):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.event_manager.post(QuitEvent())


class NotifyRoundChange(Keyboard):
    """ Realiza a notificação  de mudança de round pela ação do teclado
    """
    def notify(self,event)->None:
        if(isinstance(event, TickEvent)):
            for event in pygame.event.get():
                    if event.type == quit():
                        self.event_manager.post(QuitEvent())
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            return



class NotifyEndGame(Keyboard):
    """ Realiza a notificação  de mudança de fim de jogo pela ação do teclado
    """
    def notify(self,event)->None:
        # Get inputs
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

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