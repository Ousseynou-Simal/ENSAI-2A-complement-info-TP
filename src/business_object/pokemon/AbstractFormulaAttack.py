from business_object.pokemon.abstract_attack import AbstractAttack
from abc import abstractmethod
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
import random as rd


class AbstractFormulaAttack(AbstractAttack):

    @abstractmethod
    def get_attack_stat(APKm: AttackerPokemon):
        pass

    @abstractmethod
    def get_defense_stat(APKm: DefenderPokemon):
        pass

    def compute_damage(self, APKm1: AttackerPokemon, APKm2: DefenderPokemon):
        """"
            Calcule des dommages que fait un pokémon
        """
        damage = ((
            (
                ((2 * APKm1.level) / 5 + 2) * self.get_attack_stat(APKm1) * self._power
            ) / (self.get_defense_stat(APKm2) * 50)
            ) + 2) * rd.uniform(0.85, 1)
        return damage
