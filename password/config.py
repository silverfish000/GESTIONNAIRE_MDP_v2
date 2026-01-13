
# Les dictionnaires interdits (mdp, pseudos...)
dictionnaire_interdits = {
    # Les mots interdits de bases mais on pourra en rajouter autant qu'on veut avec le statut ADMIN
    'mdp_interdits' : [
        "", "admin", "system", "root", "config",
        "settings", "test", "temp", "default",
        "clear", "Silver", "Password", "12345678", "qwerty",
        "letmein", "welcome", "monkey", "abc123", "football", "iloveyou", "admin123",
        "password1", "12345", "123456789", "1234567890", "password!", "Passw0rd", "Admin@123",
        "Qwerty123", "Welcome1", "LetMeIn!", "Monkey@1", "Football!", "ILoveYou1",
        "1234abcd", "abcd1234", "Temp@1234", "Default1!", "Clear@2024",
        "Silver2024!", "Password2024#", "Admin2024$"
    ]
}

CARACTERES_SPECIAUX = "!@#$%^&*()_+-=}{[]|\:;<>?'\",./`~"

USERS_DATA = "data/users.json"
MDP_DATA = "data/mdp.json"