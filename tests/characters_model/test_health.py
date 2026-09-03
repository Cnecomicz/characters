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