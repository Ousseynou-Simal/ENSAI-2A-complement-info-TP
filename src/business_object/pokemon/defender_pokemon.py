from business_object.pokemon.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    # Précisons le type de pokémon dans le constructeur
    # def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
    #    # On précise uniquement le type uniquement.
    #    # Les autres variables sont a compléter lors de la création de l'instance
    #    super().__init__(stat_max, stat_current, level, name)

    # Definition de la méthode
    def get_pokemon_attack_coef(self) -> float:
        """
        Calcule des dégats pour un pokémon de type 'Défenseur'

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
