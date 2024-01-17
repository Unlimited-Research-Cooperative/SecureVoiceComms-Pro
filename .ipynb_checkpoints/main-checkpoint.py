import threading
import gpiozero
import numpy as np
import encrypt_decrypt 
import adc_dac

# Define GPIO pins for Push-to-Talk (PTT) and an indicator LED
PTT_BUTTON_PIN = 17
LED_PIN = 27

# Setup GPIO
ptt_button = gpiozero.Button(PTT_BUTTON_PIN)
led = gpiozero.LED(LED_PIN)

# Initialize ADC/DAC
adc_dac.setup()

# Pre-programmed AES256 encryption key
pre_programmed_key = b'\x9f\x15\xee\x9d\x96/OlP\xb0\x9f`lI<\xa6\x9b\xde\xdc\xc6\xf0H\xa9\xdb$\xd9\x93uS\x15k\xe1'

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

            # Encrypt the recorded audio using the pre-programmed AES256 key
            encrypted_data = encrypt_decrypt.encrypt_data(recorded_data, pre_programmed_key)  # Updated

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
            # Decrypt the received audio using the pre-programmed AES256 key
            decrypted_data = encrypt_decrypt.decrypt_data(received_encrypted_data, pre_programmed_key)  # Updated

            # Play the decrypted audio using DAC
            play_voice.play_voice(np.frombuffer(decrypted_data, dtype=np.float32))  # Function to play audio via DAC

# Running transmission and reception in parallel threads
transmission_thread = threading.Thread(target=handle_transmission)
reception_thread = threading.Thread(target=handle_reception)

transmission_thread.start()
reception_thread.start()

# Join threads if the main thread is required to stay alive
transmission_thread.join()
reception_thread.join()

