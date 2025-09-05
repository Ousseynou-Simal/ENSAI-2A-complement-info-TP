from business_object.pokemon.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):

    def __init__(self, power, name, description):
        super().__init__(power, name, description)

    def compute_damage(self, APKm1, APKm2):
        # retourne la puissance de l'attaque
        return self._power
