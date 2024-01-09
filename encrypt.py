from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_data(data, key):
    # Ensure data is in bytes
    if isinstance(data, str):
        data = data.encode()

    # Generate a random IV
    iv = os.urandom(16)

    # Add padding for AES
    pad_length = 16 - len(data) % 16
    data += bytes([pad_length] * pad_length)

    # Initialize cipher with the IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Return the IV + encrypted data
    return iv + encryptor.update(data) + encryptor.finalize()
