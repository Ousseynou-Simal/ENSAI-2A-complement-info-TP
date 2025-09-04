from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    # Précisons le type de pokémon dans le constructeur
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None):
        # On précise uniquement le type uniquement.
        # Les autres variables sont a compléter lors de la création de l'instance
        super().__init__(stat_max, stat_current, level, name, type_pk="All rounder")

    # Definition de la méthode
    def get_pokemon_attack_coef(self) -> float:
        """
        Calcule des dégats pour un pokémon de type 'Polyvalent'

        Returns :
            float : the multiplier
        """
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier


if __name__ == '__main__':
    # test de création
    print("Ok")
    pokemon = AllRounderPokemon()
    print(pokemon._type)
