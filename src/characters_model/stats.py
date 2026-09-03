from __future__ import annotations
from dataclasses import astuple, dataclass, replace

ABBREV_ATTR_MAPPING = {
    "CHA": "charisma",
    "CON": "constitution",
    "DEX": "dexterity",
    "INT": "intelligence",
    "STR": "strength",
    "WIS": "wisdom"
}

@dataclass(frozen=True)
class Stats:
    """
    An object holding a character's ability stats. Uses full names to avoid
    clash with builtins "int" and "str", but these can be accessed via dict
    notation.

    Attributes:
        charisma (int): The Charisma (CHA) score.
        constitution (int): The Constitution (CON) score.
        dexterity (int): The Dexterity (DEX) score.
        intelligence (int): The Intelligence (INT) score.
        strength (int): The Strength (STR) score.
        wisdom (int): The Wisdom (WIS) score.
    """

    charisma: int
    constitution: int
    dexterity: int
    intelligence: int
    strength: int
    wisdom: int

    def __getitem__(self, abbreviation: str) -> int:
        try:
            attr = ABBREV_ATTR_MAPPING[abbreviation.upper()]
        except (KeyError, AttributeError):
            raise KeyError(abbreviation) from None
        return getattr(self, attr)

    def as_tuple(self) -> tuple[int, int, int, int, int, int]:
        """Return the six stat values in canonical order.

        Returns:
            tuple[int, int, int, int, int, int]: A (CHA, CON, DEX, INT,
                STR, WIS) tuple of ints.
        """
        return astuple(self)

    def increment(self, abbreviation: str) -> Stats:
        """Return a copy with the declared stat increased by 1.

        Args:
            abbreviation (str): The stat to be raised.

        Returns:
            Stats: A new instance of the class with incremeneted stat.

        Raises:
            KeyError: If abbreviation is not one of the six stats.
        """
        try:
            attr = ABBREV_ATTR_MAPPING[abbreviation.upper()]
        except (KeyError, AttributeError):
            raise KeyError(abbreviation) from None
        return replace(self, **{attr: getattr(self, attr) + 1})
