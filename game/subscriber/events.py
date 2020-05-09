class Event(object):
    """Uma classe que descreve os eventos em alto nível
    """
    def __init__(self):
        self.name = "Generic Event"

    def __str__(self):
        return self.name


class QuitEvent(Event):
    """ Sair do jogo
    """
    def __init__(self):
        self.name = "Quit Event"


class TickEvent(Event):
    """Evento regular
    """
    def __init__(self):
        self.name = "Tick Event"


class InputEvent(Event):
    """ Evento de input, por meio do mouse ou teclado
    """
    def __init__(self, unicode_char, click_position):
        self.name = "Input Event"
        self.char = unicode_char
        self.click_position = click_position

    def __str__(self):
        return f"{self.name}, char={self.char}, clickpos={self.click_position}"


class InitializeEvent(Event):
    """ Inicializa tudo
    """
    def __init__(self):
        self.name = "Init Event"