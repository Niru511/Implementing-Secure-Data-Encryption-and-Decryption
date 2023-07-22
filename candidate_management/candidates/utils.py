# myapp/utils.py
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt_data(data, public_key_path):
    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher_rsa.encrypt(data.encode('utf-8'))
        return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_data(encrypted_data, private_key_path):
    encrypted_data = base64.b64decode(encrypted_data)
    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')


