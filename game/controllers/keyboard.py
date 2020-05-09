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
