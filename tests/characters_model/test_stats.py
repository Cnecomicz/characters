from pytest import raises

from characters_model.stats import Stats

# Stats exist and can be referenced in a few different ways
def test_stats_getting_values():
    stats = Stats(charisma=10, constitution=11, dexterity=12, intelligence=13, strength=14, widsom=15)
    assert stats.dexterity == 12
    assert stats["int"] == 13
    assert stats["STR"] == 14
    assert stats.as_tuple() == (10, 11, 12, 13, 14, 15)
