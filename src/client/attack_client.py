import os
import json
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Using an environment variable defined in the .env file
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        print("GET  " + url + "\n")
        req = requests.get(url)

        attack = None

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()
            # Les element qui sont renvoyés ont cette forme
            # {
            #    "name": "<An awesome name>",
            #    "attack_type": "<An awesome type>",
            #    "power": 0,
            #    "accuracy": 0,
            #    "element": "<An awesome element>",
            #    "description": "<An awesome description>"
            # }

            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")

            #   create an attack using the data contained in the json
            #   see class AttackFactory to do this
            attack = AttackFactory().instantiate_attack(
                type=raw_attack["attack_type"],
                id=raw_attack["id"],
                power=raw_attack["power"],
                name=raw_attack["name"],
                description=raw_attack["description"],
                accuracy=raw_attack["accuracy"],
                element=raw_attack["element"],
            )

        return attack

    def get_all_attacks(self) -> list(AbstractAttack):
        """
            Cette méthode renvoie la liste de toutes les attaques disponibles sous 
            la forme d'une liste d'objets AbstractAttack.
        """

        url = f"{self.__HOST}{END_POINT}/"
        print("GET  " + url + "\n")
        req = requests.get(url)

        results = []

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()

            # Création d'une liste d'objet de type
            # Récupé de chaque json
            for elm in raw_attack["results"]:
            
                #   create an attack using the data contained in the json
                #   see class AttackFactory to do this
                attack = AttackFactory().instantiate_attack(
                    type=elm["attack_type"],
                    id=elm["id"],
                    power=elm["power"],
                    name=elm["name"],
                    description=elm["description"],
                    accuracy=elm["accuracy"],
                    element=elm["element"],
                )
                results.append(attack)

        return results


# Execute Code When the File Runs as a Script
if __name__ == "__main__":
    # To load environment variables contained in the .env file
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)
