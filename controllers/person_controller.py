import json
import os
import ast
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.src.person import Person
from uuid import uuid4 as uid

from controllers.constans import dataPath

class Person_controller(object):

    def __init__(self):
        self.file = dataPath

    def create_person(self, new_person: Person = Person()):
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data["person"].append(new_person.__dict__)  # Usar __dict__ para obtener un diccionario de los atributos
            f.seek(0)
            json.dump(data, f, indent=4)  # Indent para dar formato
        f.close()
        return new_person

    def show(self):
    # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)
        return data["person"]
    

    def delete_person(self, person_id: int) -> bool:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)

            index_to_delete = None
            for index, person in enumerate(data["person"]):
                if person["_id"] == person_id:
                    index_to_delete = index
                    break

            if index_to_delete is not None:
                data["person"].pop(index_to_delete)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()  # Truncar el archivo para eliminar datos restantes
                return True

        return False

    
    def update_person(self, person_id: int, updated_data: dict) -> bool:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)

            for person in data["person"]:
                if person["_id"] == person_id:
                    person["_typePerson"] = updated_data.get("_typePerson", person["_typePerson"])
                    person["_ocupation"] = updated_data.get("_ocupation", person["_ocupation"])

                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()  # Truncar el archivo para eliminar datos restantes
                    return True

        return False
        

    