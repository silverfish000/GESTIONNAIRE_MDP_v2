MDP = "TestDeFou123"
CLE = "UKGJsbhiugm2975m021"

resultat = ""

for i in range(len(MDP)) :
    lettre_mdp = MDP[i]
    lettre_cle = CLE[i]
    nouvelle_lettre = chr(ord(lettre_mdp) ^ ord(lettre_cle))
    resultat += nouvelle_lettre

print(f"Voici ton mot de passe crypte : '{resultat}'")

original = ""

for i in range(len(MDP)) :
    lettre_mdp = resultat[i]
    lettre_cle = CLE[i]
    nouvelle_lettre = chr(ord(lettre_mdp) ^ ord(lettre_cle))
    original += nouvelle_lettre

print(original)