from config import CARACTERES_SPECIAUX, dictionnaire_interdits

class Validator:
    def __init__(self):
        pass

    def valider(self, mdp):
        if (mdp.lower() in dictionnaire_interdits['mdp_interdits']) : 
            return False, f"ERREUR : '{mdp}' est interdit"
            
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
        
        caracteres_speciaux_find = False
        for lettre in mdp :
            if (lettre in CARACTERES_SPECIAUX) :
                caracteres_speciaux_find = True
                break
        if (not caracteres_speciaux_find) :
            return False, "ERREUR : Le mot de passe doit contenir au moins un caractere special"
        
        return True, "Mot de passe valide"

validee = Validator()
resultat = validee.valider("Silver")
print(resultat)