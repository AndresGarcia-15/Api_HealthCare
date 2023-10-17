import json
import os
import ast
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
from logic.src.person import Person
from uuid import uuid4 as uid

from controllers.constans import dataPath
from logic.src.appoitments import Appoitments
from logic.src.person import Person

class Appoitments_controller(object):

    def __init__(self):
        self.file = dataPath

    def create_appoitments(self, new_appoitments: Appoitments = Appoitments()):
        
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data["appoitments"].append(new_appoitments.__dict__)  # Usar __dict__ para obtener un diccionario de los atributos
            f.seek(0)
            json.dump(data, f, indent=4)  # Indent para dar formato
        f.close()
        return new_appoitments

    def show(self):
    # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)
        return data["appoitments"]
    

    def delete_appoitments(self, person_id: int) -> bool:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)

            index_to_delete = None
            for index, person in enumerate(data["appoitments"]):
                if person["_id_cita"] == person_id:
                    index_to_delete = index
                    break

            if index_to_delete is not None:
                data["appoitments"].pop(index_to_delete)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()  # Truncar el archivo para eliminar datos restantes
                return True

        return False

    
    def update_appoitments(self, appoitments_id: int, updated_data: dict) -> bool:
        with open(self.file, 'r+', encoding='utf-8') as f:
            data = json.load(f)

            for appoitments in data["appoitments"]:
                if appoitments["_id_cita"] == appoitments_id:
                    appoitments["_date"] = updated_data.get("_date", appoitments["_date"])
                    appoitments["_time"] = updated_data.get("_time", appoitments["_time"])
                    appoitments["_doctor"] = updated_data.get("_doctor", appoitments["_doctor"])
                    appoitments["_prescription"] = updated_data.get("_prescription", appoitments["_prescription"])
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()  # Truncar el archivo para eliminar datos restantes
                    return True

        return False