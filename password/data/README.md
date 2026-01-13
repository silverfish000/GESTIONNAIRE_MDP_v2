PASSWORLD v2

Gestionnaire de mots de passe en ligne de commande, developpe en Python.

A propos :
Ce projet est une refonte complete de la v1 que vous pouvez trouver sur mon github directement. L'objectif est d'apprendre a structurer une application avec la POO, de comprendre les bases du chiffrement et de creer un outil fonctionnel pour gerer mes mots de passe en local.

Fonctionnalites :
- Systeme de connexion avec mot de passe maitre
- Ajouter / modifier / supprimer des mots de passe
- Recherche par nom
- Generateur de mots de passe personnalisable
- Chiffrement des donnees (XOR + Base64)
- Sauvegarde en JSON

Technologies :
- Python 3.x
- JSON pour le stockage
- Chiffrement maison (XOR + Base64, sans librairie externe)

Structure du projet :
- Password : represente un mot de passe (nom, mdp, url, notes, dates)
- User : represente un utilisateur (pseudo, mot de passe maitre)
- PasswordManager : gere les mots de passe (ajout, modif, suppression, sauvegarde)
- Validator : verifie la solidite des mots de passe
- Generator : genere des mots de passe aleatoires
- Crypto : chiffre et dechiffre les donnees
- App : gere l'interface en ligne de commande

Projet realise par Silver