from typing import List, Optional
from dao.type_attack_dao import TypeAttackDAO
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.attack_factory import AttackFactory


class AttackDao(metaclass=Singleton):
    def add_attack(self, attack: AbstractAttack) -> bool:
        """
        Add an attack to the database
        """
        created = False

        # Get the id type
        id_attack_type = TypeAttackDAO().find_id_by_label(attack.type)
        if id_attack_type is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tp.attack (id_attack_type, attack_name,        "
                    " power, accuracy, element, attack_description)             "
                    "VALUES                                                     "
                    "(%(id_attack_type)s, %(name)s, %(power)s, %(accuracy)s,    "
                    " %(element)s, %(description)s)                             "
                    "RETURNING id_attack;",
                    {
                        "id_attack_type": id_attack_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "description": attack.description,
                    },
                )
                res = cursor.fetchone()
        if res:
            attack.id = res["id_attack"]
            created = True

        return created

    def find_attack_by_id(self, id_attack: int) -> AbstractAttack:
        "Récupération d'un attaque a partir de l'id"

        print("ok")

        # Vérification de l'id
        if not isinstance(id_attack, int):
            return None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    # Ecriture de la requête
                    cursor.execute(
                        """SELECT at.*, at_t.attack_type_name FROM tp.attack as at
                        INNER JOIN tp.attack_type as at_t USING (id_attack_type)
                        WHERE at.id_attack = %(id_attack)s ;""",
                        {'id_attack': id_attack}
                    )
                    result = cursor.fetchone()
        except Exception as e:
            print(e)

        attack = None
        if result:
            attack = AttackFactory().instantiate_attack(
                type=result["attack_type_name"],
                id=result["id_attack"],
                power=result["power"],
                name=result["attack_name"],
                description=result["attack_description"],
                accuracy=result["accuracy"],
                element=result["element"]
            )
        
        return attack

    def find_all_attacks(self) -> List[AbsractAttack]:
        "Liste des attacks"

        # Vérification de l'id
        # if not isinstance(limit, int):
        #    return None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:

                    # Ecriture de la requête
                    cursor.execute(
                        """SELECT at.*, at_t.attack_type_name FROM tp.attack as at
                        INNER JOIN tp.attack_type as at_t USING (id_attack_type)
                        WHERE at.id_attack = %(id_attack)s ;""",
                        {'id_attack': id_attack}
                    )
                    result = cursor.fetchone()
        except Exception as e:
            print(e)

        attack = None
        if result:
            attack = AttackFactory().instantiate_attack(
                type=result["attack_type_name"],
                id=result["id_attack"],
                power=result["power"],
                name=result["attack_name"],
                description=result["attack_description"],
                accuracy=result["accuracy"],
                element=result["element"]
            )
        
        return attack


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    mon_attaque = PhysicalFormulaAttack(
        power=50,
        name="chatouille",
        description="guili-guilis",
        accuracy=90,
        element="Normal",
    )

    # succes = AttackDao().add_attack(mon_attaque)
    # print("Attack created in database : " + str(succes))

    succes = AttackDao().find_attack_by_id(id_attack=3)
    print(succes)









Boucle sur les dictionnaire:

    - Grace à 1 dictionnaire => on créé un objet
    - ajoute lobjct a une liste

retourne la liste 



