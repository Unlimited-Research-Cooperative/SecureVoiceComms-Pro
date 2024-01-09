from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

# Function to generate DH parameters and private key
def generate_private_key():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    return parameters.generate_private_key()

# Function to serialize public key
def serialize_public_key(public_key):
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

# Function to deserialize a peer's public key
def deserialize_peer_public_key(peer_public_key_bytes):
    return serialization.load_pem_public_key(
        peer_public_key_bytes,
        backend=default_backend()
    )

# Function to perform the key exchange
def perform_key_exchange(private_key, peer_public_key_bytes):
    peer_public_key = deserialize_peer_public_key(peer_public_key_bytes)
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

# Function to derive a symmetric key from the shared secret
def derive_symmetric_key(shared_key):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    )
    return hkdf.derive(shared_key)

# Example usage:
# private_key = generate_private_key()
# my_public_key_bytes = serialize_public_key(private_key.public_key())
# Send `my_public_key_bytes` to peer and receive `peer_public_key_bytes`
# shared_key = perform_key_exchange(private_key, peer_public_key_bytes)
# symmetric_key = derive_symmetric_key(shared_key)
