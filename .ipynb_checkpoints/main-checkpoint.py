import threading
import gpiozero  # For handling GPIO pins on Raspberry Pi
import voice_processing
import encrypt
import decrypt
import play_voice
import numpy as np
# Import hypothetical transmit and receive modules (to be implemented based on specific hardware)
import transmit
import receive

# Define GPIO pins for Push-to-Talk (PTT) and an indicator LED
PTT_BUTTON_PIN = 17  # Example GPIO pin number for the PTT button
LED_PIN = 27  # Example GPIO pin number for an LED indicator

# Setup GPIO
ptt_button = gpiozero.Button(PTT_BUTTON_PIN)
led = gpiozero.LED(LED_PIN)

# Encryption key (ensure it's 32 bytes for AES-256)
encryption_key = b'your-32-byte-encryption-key-here'

def handle_transmission():
    """
    Handles the recording and transmission of audio when PTT button is pressed.
    """
    while True:
        if ptt_button.is_pressed:
            led.on()  # Turn on the LED to indicate recording
            print("Recording...")
            recorded_data = voice_processing.record_voice(duration=5)
            encrypted_data = encrypt.encrypt_data(recorded_data.tobytes(), encryption_key)

            # Transmit the encrypted data
            transmit.send(encrypted_data)  # Hypothetical function (radio hardware specific)
            led.off()  # Turn off the LED after transmission

def handle_reception():
    """
    Continuously listens for incoming transmissions, decrypts, and plays them.
    """
    while True:
        received_encrypted_data = receive.receive()  # Hypothetical function (radio hardware specific)
        if received_encrypted_data:
            decrypted_data = decrypt.decrypt_data(received_encrypted_data, encryption_key)
            play_voice.play_voice(np.frombuffer(decrypted_data, dtype=np.float32))

# Running transmission and reception in parallel threads
transmission_thread = threading.Thread(target=handle_transmission)
reception_thread = threading.Thread(target=handle_reception)

transmission_thread.start()
reception_thread.start()

# Optionally join threads if needed
# transmission_thread.join()
# reception_thread.join()

