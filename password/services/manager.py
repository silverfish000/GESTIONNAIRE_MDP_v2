from services.crypto import Crypto
from services.validator import Validator
from services.generator import Generator
from config import PASSWORDS_FILE
import json
import os

class Manager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.crypto = Crypto(master_password)
        self.validator = Validator()
    def _load_password(self) :
        if os.path.exists(PASSWORDS_FILE):
            try:
                file = open(PASSWORDS_FILE, 'r')
                data = json.load(file)
                file.close()
                return data
            except json.JSONDecodeError:
                print("Fichier non existant")
                return {}
        else:
            return {}
    def _save_passwords(self, passwords_dict):
        directory = os.path.dirname(PASSWORDS_FILE)

        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open(PASSWORDS_FILE, "w")
        json.dump(passwords_dict, file, indent=4)
        file.close()
            

if __name__ == "__main__":
    manager = Manager("MonMotDePasse123")
    print("Manager init !")



# _0_