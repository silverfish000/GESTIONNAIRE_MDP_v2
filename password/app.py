from services.manager import Manager
import sys


class PasswordApp:
    def __init__(self):
        self.manager = None
        self.running = True
    
    def start(self):
        print("=" * 50)
        print("  GESTIONNAIRE DE MOTS DE PASSE v2")
        print("=" * 50)
        
        master_password = input("\nEntrez votre mot de passe maitre : ")
        
        self.manager = Manager(master_password)
        
        print("Authentifie avec succes !\n")
        
        while self.running:
            self.show_menu()
            self.handle_choice()
    
    def show_menu(self):
        print("\n" + "=" * 50)
        print("MENU PRINCIPAL")
        print("=" * 50)
        print("1. Ajouter un mot de passe")
        print("2. Recuperer un mot de passe")
        print("3. Lister tous les services")
        print("4. Supprimer un mot de passe")
        print("5. Quitter")
        print("=" * 50)
    
    def handle_choice(self):
        choice = input("\nVotre choix : ")
        
        if choice == "1":
            self.add_password()
        elif choice == "2":
            self.get_password()
        elif choice == "3":
            self.list_passwords()
        elif choice == "4":
            self.delete_password()
        elif choice == "5":
            self.quit_app()
        else:
            print("Choix invalide")
    
    def add_password(self):
        print("\n--- AJOUTER UN MOT DE PASSE ---")
        service = input("Nom du service : ")
        username = input("Nom d'utilisateur : ")
        
        choice = input("Generer un mot de passe ? (o/n) : ")
        
        if choice.lower() == "o":
            password = self.manager.add(service, username)
        else:
            password_input = input("Mot de passe : ")
            password = self.manager.add(service, username, password_input)
        
        if password:
            print(f"\nMot de passe enregistre !")
            print(f"NOTEZ-LE : {password}")
            input("\nAppuyez sur Entree pour continuer...")
    
    def get_password(self):
        print("\n--- RECUPERER UN MOT DE PASSE ---")
        service = input("Nom du service : ")
        
        info = self.manager.get(service)
        
        if info:
            print(f"\nService  : {info['service']}")
            print(f"Username : {info['username']}")
            print(f"Password : {info['password']}")
            input("\nAppuyez sur Entree pour continuer...")
    
    def list_passwords(self):
        print("\n--- LISTE DES SERVICES ---")
        
        services = self.manager.list_all()
        
        if services:
            for s in services:
                print(f"  - {s['service']} ({s['username']})")
        
        input("\nAppuyez sur Entree pour continuer...")
    
    def delete_password(self):
        print("\n--- SUPPRIMER UN MOT DE PASSE ---")
        service = input("Nom du service : ")
        
        confirm = input(f"Confirmer la suppression de '{service}' ? (o/n) : ")
        
        if confirm.lower() == "o":
            self.manager.delete(service)
            input("\nAppuyez sur Entree pour continuer...")
    
    def quit_app(self):
        print("\nAu revoir !")
        self.running = False


if __name__ == "__main__":
    app = PasswordApp()
    app.start()