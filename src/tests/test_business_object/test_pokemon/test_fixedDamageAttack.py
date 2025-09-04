from business_object.pokemon.fixedDamageAttack import FixedDamageAttack


class TestFixedDamageAttack:

    def test_compute_damage(self):
        # GIVEN
        attaque = FixedDamageAttack(power=10, name='attake 1', description='text')

        # WHEN
        power = attaque.compute_damage()

        # THEN
        assert power == 10


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
