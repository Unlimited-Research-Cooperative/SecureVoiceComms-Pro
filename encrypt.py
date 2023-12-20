from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_data(data, key):
    # Ensure data is in bytes
    if isinstance(data, str):
        data = data.encode()

    # Add padding for AES
    pad_length = 16 - len(data) % 16
    data += bytes([pad_length] * pad_length)

    # Initialize cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(os.urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()

    return encryptor.update(data) + encryptor.finalize()
