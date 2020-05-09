import pygame
from game.subscriber.events import *


class Keyboard(object):
    """ Trata dos inputs do teclado
    """
    def __init__(self, event_manager, model) -> None:

        self.event_manager = event_manager
        self.model = model
        ## Subscribe listener
        self.event_manager.subscribe_listener(self)

    def notify(self, event) -> None:
        """ Notifica o teclado se o usuário pressionar alguma tecla
        """
        if (isinstance(event, TickEvent)):
            # Chamada a cada frame do jogo, aqui é onde
            # checamos as teclas pressionadas
            for event in pygame.event.get():
                # Se a janela fechar
                if (event.type == pygame.QUIT):
                    self.event_manager.post(QuitEvent())
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        self.event_manager.post(StateChangeEvent(None))
                    else:
                        self.keydown_play(event)

    def keydown_play(self, event):
        """ Gerencia as teclas apertadas durante o jogo
        """
        self.event_manager.post(InputEvent(event.unicode, None))
