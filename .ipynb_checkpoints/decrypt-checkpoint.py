from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_data(encrypted_data, key):
    # Assuming the IV is the first 16 bytes of the encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Initialize cipher with the IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    pad_length = decrypted_data[-1]
    return decrypted_data[:-pad_length]
