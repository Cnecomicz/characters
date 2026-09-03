from pytest import raises

from characters_model.health import Health

# Health tracks current and max, and can take damage and heal
def test_health_exists_and_can_lose_and_gain():
    health_1 = Health(current=10, maximum=10)
    assert health_1.current == 10
    assert health_1.maximum == 10
    health_2 = health_1.damaged(4)
    assert health_2.current == 6
    assert health_2.maximum == 10
    health_3 = health_2.healed(3)
    assert health_3.current == 9
    assert health_3.maximum == 10
    health_4 = health_3.healed(100)
    assert health_4.current == 10
    assert health_4.maximum == 10

# Maximum must be positive and current cannot exceed maximum
def test_health_well_formedness():
    with raises(ValueError):
        Health(current=0, maximum=0)
    with raises(ValueError):
        Health(current=20, maximum=10)

# Health tracks negative hitpoints
def test_health_knows_non_positive_current_and_how_much():
    health_1 = Health(current=1, maximum=10)
    assert not health_1.is_at_or_below_zero
    assert health_1.damage_below_zero == 0
    health_2 = Health(current=0, maximum=10)
    assert health_2.is_at_or_below_zero
    assert health_2.damage_below_zero == 0
    health_3 = Health(current=-3, maximum=10)
    assert health_3.is_at_or_below_zero
    assert health_3.damage_below_zero == 3