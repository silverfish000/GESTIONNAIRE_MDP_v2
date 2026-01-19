from services.crypto import Crypto
from services.validator import Validator
from services.generator import Generator
from config import PASSWORDS_FILE
import json
import os


class Manager:
    def __init__(self, master_password):
        self.master_password = master_password
        pass
    
    
    # ==================== MÉTHODES PRIVÉES (HELPERS) ====================
    
    def _load_passwords(self):
        """
        Charge les mots de passe depuis le fichier JSON
        
        Returns:
            dict: Dictionnaire des mots de passe chiffrés
        """
        pass
    
    
    def _save_passwords(self, passwords_dict):
        """
        Sauvegarde les mots de passe dans le fichier JSON
        
        Args:
            passwords_dict (dict): Dictionnaire à sauvegarder
        """
        pass
    
    
    # ==================== MÉTHODES PUBLIQUES (CRUD) ====================
    
    def add(self, service, username, password=None):
        
        """
        Ajoute un nouveau mot de passe
        
        Args:
            service (str): Nom du service (ex: "Gmail")
            username (str): Identifiant utilisateur
            password (str, optional): Mot de passe (généré si None)
        
        Returns:
            str: Le mot de passe ajouté (en clair)
        """
        pass
    
    
    def get(self, service):
        """
        Récupère un mot de passe déchiffré
        
        Args:
            service (str): Nom du service
        
        Returns:
            dict: {"service": ..., "username": ..., "password": ...}
            None: Si le service n'existe pas
        """
        pass
    
    
    def list_all(self):
        """
        Liste tous les services enregistrés (SANS les mots de passe)
        
        Returns:
            list: Liste des services avec leurs usernames
        """
        pass
    
    
    def update(self, service, new_password=None):
        """
        Met à jour un mot de passe existant
        
        Args:
            service (str): Nom du service
            new_password (str, optional): Nouveau mot de passe (généré si None)
        
        Returns:
            str: Le nouveau mot de passe
        """
        pass
    
    
    def delete(self, service):
        """
        Supprime un mot de passe
        
        Args:
            service (str): Nom du service
        
        Returns:
            bool: True si supprimé, False si n'existe pas
        """
        pass