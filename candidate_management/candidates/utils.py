# myapp/utils.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt_string_rsa(message):
    byte_message = str.encode(message)
    with open('public_key.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_string = cipher.encrypt(byte_message)
    encrypted_string = base64.b64encode(encrypted_string).decode('utf-8')
    return encrypted_string


def decrypt_string_rsa(encrypted_string):
    decoded_hash_string = base64.b64decode(encrypted_string)
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    result_string = cipher.decrypt(decoded_hash_string).decode()

    return result_string



