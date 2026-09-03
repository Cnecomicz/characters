from __future__ import annotations
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Health:
    """A current/maximum hitpoint pair.

    Attributes:
        current (int): The current hitpoints.
        maximum (int): The maximum hitpoints.
    """

    current: int
    maximum: int

    def __post_init__(self) -> None:
        if self.maximum <= 0:
            raise ValueError(
                f"Maximum is {self.maximum} but must be at least 1."
            )
        if self.current > self.maximum:
            raise ValueError(
                f"Current is {self.current} but cannot exceed {self.maximum}."
            )

    @property
    def damage_below_zero(self) -> int:
        """How far below 0 current has fallen.

        Returns:
            int: The distance between current and 0, or 0 if current is
                positive.
        """
        return max(0, -self.current)

    @property
    def is_at_or_below_zero(self) -> bool:
        """Whether current is less than or equal to 0.

        Returns:
            bool: True if current is non positive.
        """
        return self.current <= 0

    def damaged(self, amount: int) -> Health:
        """Return a new Health instance after taking amount damage.

        Args:
            amount (int): The amount of damage to subtract from current.

        Returns:
            Health: A new Health instance with damage applied.
        """
        return replace(self, current=self.current-amount)

    def healed(self, amount: int) -> Health:
        """Return a new Health instance after healing amount damage. Cannot
        raise current above maximum.

        Args:
            amount (int): The amount of hitpoints to add to current.

        Returns:
            Health: A new Health instance with healing applied.
        """
        return replace(self, current=min(self.current+amount, self.maximum))