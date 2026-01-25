import base64


class Crypto:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        encrypted_password = ''
        for i in range(len(text)):
            letter = text[i]
            key_letter = self.key[i % len(self.key)]
            new_letter = chr(ord(letter) ^ ord(key_letter))
            encrypted_password += new_letter
        return base64.b64encode(encrypted_password.encode("latin-1")).decode()

    def decrypt(self, encrypted_text):
        encrypted_text = base64.b64decode(encrypted_text.encode()).decode("latin-1")
        decrypted_password = ''
        for i in range(len(encrypted_text)):
            letter = encrypted_text[i]
            key_letter = self.key[i % len(self.key)]
            new_letter = chr(ord(letter) ^ ord(key_letter))
            decrypted_password += new_letter
        return decrypted_password


my_crypto = Crypto("MonMotDePasse123")
result = my_crypto.encrypt("Laviedemameremetrouvepas")

# _0_