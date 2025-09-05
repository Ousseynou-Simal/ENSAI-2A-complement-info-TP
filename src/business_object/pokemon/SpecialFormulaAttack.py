from business_object.pokemon.AbstractFormulaAttack import AbstractFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon


class SpecialFormulaAttack(AbstractFormulaAttack):

    def get_attack_stat(APKm: AttackerPokemon):
        return APKm.sp_atk_current

    def get_defense_stat(APKm: DefenderPokemon):
        return APKm.sp_def_current
