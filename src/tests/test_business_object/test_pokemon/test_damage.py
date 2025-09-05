from business_object.pokemon.PhysicalFormulaAttack import PhysicalFormulaAttack
# from business_object.pokemon.SpecialFormulaAttack import SpecialFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestPhysicalFormulaAttack:

    def test_damage_physicalattak(self):
        # GIVEN
        pokemon_attaque = AttackerPokemon(level=3, stat_current=Statistic(attack=10))
        pokemon_defense = DefenderPokemon(level=2, stat_current=Statistic(defense=10))

        attaque = PhysicalFormulaAttack(power=10)

        # WHEN
        damage = attaque.compute_damage(APKm1=pokemon_attaque, APKm2=pokemon_defense)
        return damage


if __name__ == '__main__':
    test = TestPhysicalFormulaAttack()
    print(test._power)
    # print(test.test_damage_physicalattak())
