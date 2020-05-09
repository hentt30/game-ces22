from game.subscriber.events import *


class GameEngine:
    """ Controla o jogo
    """
    def __init__(self, event_manager) -> None:

        self.event_manager = event_manager
        self.event_manager.subscribe_listener(self)
        self.keep_going = False

    def notify(self, event) -> None:
        """ Receber a notificação do gerenciador de eventos
        """
        if (isinstance(event, QuitEvent)):
            self.keep_going = False

    def run(self):
        """ Inicia o  jogo
        """
        self.keep_going = True
        self.event_manager.post(InitializeEvent())

        while self.keep_going:
            new_tick = TickEvent()
            self.event_manager.post(new_tick)
