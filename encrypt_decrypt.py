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

def decrypt_data(encrypted_data, key):
    # Extract the IV from the beginning of the encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Initialize cipher with the extracted IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    pad_length = decrypted_data[-1]
    return decrypted_data[:-pad_length]