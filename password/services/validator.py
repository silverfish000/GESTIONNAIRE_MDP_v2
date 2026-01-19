from config import SPECIAL_CHARACTERS, forbidden_dictionary


class Validator:
    def __init__(self):
        pass

    def validate(self, password):
        if password.lower() in forbidden_dictionary['forbidden_passwords']:
            return False, f"ERREUR : '{password}' est interdit"

        if len(password) < 8:
            return False, "ERREUR : Mot de passe trop court"

        uppercase_found = False
        for char in password:
            if char.isupper():
                uppercase_found = True
                break
        if not uppercase_found:
            return False, "ERREUR : Le mot de passe doit contenir au moins une majuscule"

        lowercase_found = False
        for char in password:
            if char.islower():
                lowercase_found = True
                break
        if not lowercase_found:
            return False, "ERREUR : Le mot de passe doit contenir au moins une minuscule"

        digit_found = False
        for char in password:
            if char.isdigit():
                digit_found = True
                break
        if not digit_found:
            return False, "ERREUR : Le mot de passe doit contenir au moins un chiffre"

        special_character_found = False
        for char in password:
            if char in SPECIAL_CHARACTERS:
                special_character_found = True
                break
        if not special_character_found:
            return False, "ERREUR : Le mot de passe doit contenir au moins un caractere special"

        return True, "Mot de passe valide"


validator = Validator()
result = validator.validate("Silver")

# _0_