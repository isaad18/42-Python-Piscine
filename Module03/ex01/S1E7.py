from S1E9 import Character


class Baratheon(Character):
    """A class representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(
            first_name,
            is_alive
        )
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """A class representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(
            first_name,
            is_alive
        )
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Creates and returns a new Lannister instance."""
        return cls(first_name, is_alive)
