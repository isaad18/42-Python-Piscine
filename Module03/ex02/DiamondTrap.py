from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing the King with diamond inheritance."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize King with Baratheon's physical characteristics."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, color: str) -> None:
        """Set the eye color of the King."""
        self.eyes = color

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def set_hairs(self, color: str) -> None:
        """Set the hair color of the King, replacing the hair attribute."""
        self.hairs = color

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs

    def __str__(self):
        """Return string representation of the King."""
        hairs = getattr(self, 'hairs', getattr(self, 'hair', None))
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{hairs}')"

    def __repr__(self):
        """Return repr representation of the King."""
        hairs = getattr(self, 'hairs', getattr(self, 'hair', None))
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{hairs}')"
