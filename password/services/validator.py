from config import CARACTERES_SPECIAUX, dictionnaire_interdits

class Validator:
    def __init__(self):
        pass

    def valider(self, mdp):
        if (len(mdp) < 8) :
            return False, "ERREUR : Mot de passe trop court"

        majuscule_find = False
        for lettre in mdp :
            if (lettre.isupper()) :
                majuscule_find = True
                break
        if (not majuscule_find) :
            return False, "ERREUR : Le mot de passe doit contenir au moins une majuscule"
        
        minuscule_find = False
        for lettre in mdp :
            if (lettre.islower()) :
                minuscule_find = True
                break
        if (not minuscule_find) :
            return False, "ERREUR : Le mot de passe doit contenir au moins une minuscule"
        
        chiffre_find = False
        for lettre in mdp :
            if (lettre.isdigit()) :
                chiffre_find = True
                break
        if (not chiffre_find) :
            return False, "ERREUR : Le mot de passe doit contenir au moins un chiffre"

validee = Validator()
resultat = validee.valider("TestDefou123&")
print(resultat)