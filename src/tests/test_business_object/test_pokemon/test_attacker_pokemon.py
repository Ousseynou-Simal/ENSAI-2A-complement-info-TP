from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    """Cette classe permet de réaliser des tests sur la méthode de calcule"""

    def test_get_pokemon_attack_coef(self):
        # GIVEN
        pokemon = AttackerPokemon(stat_current=Statistic(speed=200, attack=200))

        # WHEN
        multiplier = pokemon.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 3


if __name__ == '__main__':
    import pytest

    # cette commande permet de lancer les test grace a l'exécution du fichier avec la flèche
    pytest.main([__file__])
