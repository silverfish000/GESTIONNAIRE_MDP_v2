import base64

class Crypto:
    def __init__(self, cle):
        self.cle = cle
    def chiffrer(self, texte):
        mdp_chiffre = ''
        for i in range(len(texte)) :
            lettre = texte[i]
            lettre_cle = self.cle[i % len(self.cle)]
            nouvelle_lettre = chr(ord(lettre) ^ ord(lettre_cle))
            mdp_chiffre += nouvelle_lettre
        return base64.b64encode(mdp_chiffre.encode("latin-1")).decode()
            
    def dechiffrer(self, texte_chiffre) :
        texte_chiffre = base64.b64decode(texte_chiffre.encode()).decode("latin-1")
        mdp_dechiffre = ''
        for i in range(len(texte_chiffre)) :
            lettre = texte_chiffre[i]
            lettre_cle = self.cle[i % len(self.cle)]
            nouvelle_lettre = chr(ord(lettre) ^ ord(lettre_cle))
            mdp_dechiffre += nouvelle_lettre
        return mdp_dechiffre


mon_crypto = Crypto("MonMotDePasse123")
resultat = mon_crypto.chiffrer("TestDeFofsfsfsu1234%$")

print(f"Voici ton mot de passe chiffre : '{resultat}'")
resultat_dechiffrer = mon_crypto.dechiffrer(resultat)
print(f"Voici ton mot de passe dechiffre : '{resultat_dechiffrer}'")
