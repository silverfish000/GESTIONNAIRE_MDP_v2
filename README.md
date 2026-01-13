PASSWORLD v2

Gestionnaire de mots de passe en ligne de commande, developpe en Python.

Objectifs du projet :
- POO : Architecture en classes (Password, User, PasswordManager...)
- Chiffrement : Securisation des donnees avec cryptography
- Stockage JSON : Persistance des donnees entre les sessions
- Validation avancee : Regles de securite pour les mots de passe
- Generateur : Creation de mots de passe aleatoires securises

Fonctionnalites :
- Systeme de connexion avec mot de passe maitre
- Ajouter / modifier / supprimer des mots de passe
- Recherche par nom
- Generateur de mots de passe personnalisable
- Chiffrement des donnees sensibles
- Sauvegarde automatique en JSON

Technologies :
- Python 3.x
- cryptography (chiffrement Fernet)
- JSON (stockage)

POO (Architecture du programme):

Password        --> UN mot de passe (nom, mdp, url, notes, dates)
User            --> UN utilisateur (pseudo, mot de passe maitre hashe)
PasswordManager --> Gere la collection de mots de passe (CRUD + sauvegarde JSON)
Validator       --> Valide les mots de passe selon les regles
Generator       --> Genere des mots de passe aleatoires
Crypto          --> Chiffre/dechiffre les donnees
App             --> Gere les menus CLI et le flux de l'application