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