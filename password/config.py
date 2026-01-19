# Forbidden dictionaries (passwords, usernames...)
forbidden_dictionary = {
    # Basic forbidden words, more can be added later with ADMIN status
    'forbidden_passwords': [
        "", " ", "admin", "system", "root", "config",
        "settings", "test", "temp", "default",
        "clear", "silver", "password", "12345678", "qwerty",
        "letmein", "welcome", "monkey", "abc123", "football", "iloveyou", "admin123",
        "password1", "12345", "123456789", "1234567890", "password!", "passw0rd", "admin@123",
        "qwerty123", "welcome1", "letmein!", "monkey@1", "football!", "iloveyou1",
        "1234abcd", "abcd1234", "temp@1234", "default1!", "clear@2024",
        "silver2024!", "password2024#", "admin2024$"
    ]
}

SPECIAL_CHARACTERS = "!@#$%^&*()_+-=}{[]|\\:;<>?'\",./`~"

USERS_DATA_PATH = "data/users.json"
PASSWORDS_DATA_PATH = "data/mdp.json"


# _0_