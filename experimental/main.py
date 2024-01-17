import threading
import gpiozero
import voice_processing
import encrypt
import decrypt
import play_voice
import adc_dac
import key_share
import numpy as np

# Define GPIO pins for Push-to-Talk (PTT) and an indicator LED
PTT_BUTTON_PIN = 17
LED_PIN = 27

# Setup GPIO
ptt_button = gpiozero.Button(PTT_BUTTON_PIN)
led = gpiozero.LED(LED_PIN)

# Initialize ADC/DAC
adc_dac.setup()

# Generate private key using key_share.py
private_key = key_share.generate_private_key()

# Serialize public key to send to peer
my_public_key_bytes = key_share.serialize_public_key(private_key.public_key())

# Function to simulate sending public key to peer and receiving peer's public key
def exchange_public_keys(my_public_key_bytes):
    # Simulate sending and receiving public key bytes
    # In a real application, you would send and receive this over a secure channel
    peer_public_key_bytes = my_public_key_bytes  # In reality, this would be from the peer
    return peer_public_key_bytes

# Receive peer's public key bytes
peer_public_key_bytes = exchange_public_keys(my_public_key_bytes)

# Perform key exchange to get shared key
shared_key = key_share.perform_key_exchange(private_key, peer_public_key_bytes)

# Derive symmetric encryption key
encryption_key = key_share.derive_symmetric_key(shared_key)

def handle_transmission():
    """
    Handles the recording and transmission of audio when PTT button is pressed.
    """
    while True:
        if ptt_button.is_pressed:
            led.on()  # Indicate recording
            print("Recording...")

            # Record audio using ADC
            recorded_data = adc_dac.read_from_adc()  # Function to read from ADC

            # Encrypt the recorded audio
            encrypted_data = encrypt.encrypt_data(recorded_data, encryption_key)

            # Transmit the encrypted data through your dongle
            adc_dac.write_to_dac(encrypted_data)  # Function to write to DAC for transmission

            led.off()  # Turn off the LED after transmission

def handle_reception():
    """
    Continuously listens for incoming transmissions, decrypts, and plays them.
    """
    while True:
        # Receive encrypted data through your dongle
        received_encrypted_data = adc_dac.read_from_adc()  # Function to read from ADC for reception

        if received_encrypted_data:
            # Decrypt the received audio
            decrypted_data = decrypt.decrypt_data(received_encrypted_data, encryption_key)

            # Play the decrypted audio using DAC
            play_voice.play_voice(np.frombuffer(decrypted_data, dtype=np.float32))  # Function to play audio via DAC

# Running transmission and reception in parallel threads
transmission_thread = threading.Thread(target=handle_transmission)
reception_thread = threading.Thread(target=handle_reception)

transmission_thread.start()
reception_thread.start()

# Join threads if main thread is required to stay alive
transmission_thread.join()
reception_thread.join()

