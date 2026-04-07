from abc import ABC, abstractmethod


class Character(ABC):
    """A class representing the base character."""
    first_name: str
    is_alive: bool

    @abstractmethod
    def __init__(
        self,
        first_name: str,
        is_alive: bool = True
    ):
        """Initializes the character with the given attributes.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Sets is_alive to False."""
        self.is_alive = False


class Stark(Character):
    """A class representing the Stark family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initializes the Stark character with the given attributes.
        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): Whether the character is alive.
                Defaults to True.
        """
        super().__init__(first_name, is_alive)
