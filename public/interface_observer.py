from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        """
        Attach an observer to the subject
        """
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        """
        Unsubscribe an observer from the subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event
        """
        pass


class Observer(ABC):
    """
    The Observer interface declares the update method,used by subjects
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recieve updates from subject
        """
        pass
