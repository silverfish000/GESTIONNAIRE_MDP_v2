
# Les dictionnaires interdits (mdp, pseudos...)
dictionnaire_interdits = {
    # Les mots interdits de bases mais on pourra en rajouter autant qu'on veut avec le statut ADMIN
    'mdp_interdits' : [
        "", "admin", "system", "root", "config",
        "settings", "test", "temp", "default",
        "clear", "silver", "password", "12345678", "qwerty",
        "letmein", "welcome", "monkey", "abc123", "football", "iloveyou", "admin123",
        "password1", "12345", "123456789", "1234567890", "password!", "passw0rd", "admin@123",
        "qwerty123", "welcome1", "letmein!", "monkey@1", "football!", "iloveyou1",
        "1234abcd", "abcd1234", "temp@1234", "default1!", "clear@2024",
        "silver2024!", "password2024#", "admin2024$"
    ]
}

CARACTERES_SPECIAUX = "!@#$%^&*()_+-=}{[]|\:;<>?'\",./`~"

USERS_DATA = "data/users.json"
MDP_DATA = "data/mdp.json"