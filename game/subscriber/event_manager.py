from weakref import WeakKeyDictionary


class EventManager(object):
    """ Essa classe é responsável por receber os eventos e notificar os objetos competententes
    """
    def __init__(self) -> None:
        self.listeners = WeakKeyDictionary()

    def subscribe_listener(self, listener) -> None:
        """Registra um objeto para receber notificações de event Manager
        """
        self.listeners[listener] = 1

    def unsubscribe_listener(self, listener) -> None:
        """Retira um objeto da lista de inscritos
        """
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event) -> None:
        """ Avisa os inscritos que ocorreu algum evento
        """
        for listener in self.listeners.keys():
            listener.notify(event)
