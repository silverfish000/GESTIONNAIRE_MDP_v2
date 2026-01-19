import random
from config import LOWERCASE, UPPERCASE, DIGITS, SPECIAL_CHARACTERS
from services.validator import Validator

class Generator:
    
    @staticmethod
    def generate(length=16, use_upper=True, use_lower=True, 
             use_digits=True, use_special=True):
        characters = ""
        if use_lower:
            characters += LOWERCASE
        
        if use_upper:
            characters += UPPERCASE
        
        if use_digits:
            characters += DIGITS
        
        if use_special:
            characters += SPECIAL_CHARACTERS
        
        validator = Validator()
        
        max_attempts = 100
        attempts = 0
        while attempts < max_attempts :
            password = ""
            for _ in range(length) :
                password += random.choice(characters)
            is_valid, message = validator.validate(password)
            if is_valid :
                return password
            attempts += 1
            
        raise ValueError(f"Impossible de generer un mot de passe apres {max_attempts} tentatives. Veuillez recommencez")
        
if __name__ == "__main__":
    print(Generator.generate())


# _0_