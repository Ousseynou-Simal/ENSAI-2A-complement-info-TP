from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon:

    def test_get_pokemon_attack_coef(self):
        # Réalisation du test

        # GIVEN
        pokemon = AllRounderPokemon(stat_current=Statistic(sp_atk=300, sp_def=300))

        # WHEN
        multiplier = pokemon.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 4


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
