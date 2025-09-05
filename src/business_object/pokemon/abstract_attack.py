from abc import ABC, abstractmethod
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, APkm1: AttackerPokemon, APkm2: AttackerPokemon) -> int:
        pass

# Création de la clase
