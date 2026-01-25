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
    
    def _load_password(self):
        if os.path.exists(PASSWORDS_FILE):
            try:
                file = open(PASSWORDS_FILE, 'r')
                data = json.load(file)
                file.close()
                return data
            except json.JSONDecodeError:
                print("Fichier JSON corrompu")
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
    
    def add(self, service, username, password=None):
        if password is None:
            password = Generator.generate()
        
        is_valid, message_validator = self.validator.validate(password)
        if not is_valid:
            print(f"❌ {message_validator}")
            return None
        
        passwords = self._load_password()
        
        if service in passwords:
            print(f"❌ Service '{service}' existe déjà")
            return None
        
        encrypted_password = self.crypto.encrypt(password)
        passwords[service] = {
            "username": username,
            "password": encrypted_password
        }
        
        self._save_passwords(passwords)
        print(f"Mot de passe ajoute pour '{service}'")
        return password
    
    def get(self, service):
        passwords = self._load_password()
        
        if service not in passwords:
            print(f"❌ Service '{service}' introuvable")
            return None
        
        data = passwords[service]
        decrypted_password = self.crypto.decrypt(data["password"])
        
        return {
            "service": service,
            "username": data["username"],
            "password": decrypted_password
        }
    def list_all(self):
        passwords = self._load_password()
        
        if not passwords:
            print("Aucun mot de passe enregistré")
            return [] # En gros je return rien (dico)
        

        services = []
        for service, data in passwords.items():
            services.append({
                "service": service,
                "username": data["username"]
            })
        
        return services
    def delete(self, service):
        passwords = self._load_password()
        
        if service not in passwords:
            print(f"Service '{service}' introuvable")
            return False
        
        new_passwords = {}
        for key, value in passwords.items():
            if key != service:
                new_passwords[key] = value
        
        self._save_passwords(new_passwords)
        
        print(f"'{service}' supprimé")
        return True


if __name__ == "__main__":
    manager = Manager("MonMotDePasse123!")
    
    # TEST POUR ADD
    pwd = manager.add("Google", "test@gmail.com")
    if pwd:
        print(f"Mot de passe ajouté : {pwd}")
    
    # TEST POUR GET
    info = manager.get("Google")
    if info:
        print(f"\nRecuperation du service '{info['service']}' :")
        print(f"   Username: {info['username']}")
        print(f"   Password: {info['password']}")

# _0_