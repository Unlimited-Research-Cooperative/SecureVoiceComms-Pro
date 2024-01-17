import time
import numpy as np
import busio
from gpiozero import DigitalOutputDevice
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_mcp4725 import MCP4725
import board

# Import encryption and decryption modules
from encrypt_decrypt import encrypt_data, decrypt_data

# Define ADC and DAC channel addresses for microphone and headphone paths
MIC_ADC_ADDRESS = 0x48
MIC_DAC_ADDRESS = 0x60

HEADPHONE_ADC_ADDRESS = 0x49
HEADPHONE_DAC_ADDRESS = 0x61

# Define GPIO pin for PTT
PTT_PIN = 17

def setup():
    global i2c_mic, adc_mic, dac_mic, i2c_headphone, adc_headphone, dac_headphone, ptt

    i2c_mic = busio.I2C(board.SCL, board.SDA)

    # Initialize ADC for microphone input
    ads_mic = ADS1115(i2c_mic, address=MIC_ADC_ADDRESS)
    adc_channel_mic = AnalogIn(ads_mic, ADS.P0)

    # Initialize DAC for microphone output
    dac_mic = MCP4725(i2c_mic, address=MIC_DAC_ADDRESS)

    i2c_headphone = busio.I2C(board.SCL, board.SDA)

    # Initialize ADC for headphone input
    ads_headphone = ADS1115(i2c_headphone, address=HEADPHONE_ADC_ADDRESS)
    adc_channel_headphone = AnalogIn(ads_headphone, ADS.P1)

    # Initialize DAC for headphone output
    dac_headphone = MCP4725(i2c_headphone, address=HEADPHONE_DAC_ADDRESS)

    # GPIO setup for PTT
    ptt = DigitalOutputDevice(PTT_PIN)

def activate_ptt():
    ptt.on()

def deactivate_ptt():
    ptt.off()

def read_adc_mic():
    return adc_channel_mic.value

def read_adc_headphone():
    return adc_channel_headphone.value

def write_dac_mic(value):
    dac_mic.normalized_value = value / 65535

def write_dac_headphone(value):
    dac_headphone.normalized_value = value / 65535

def record_audio_mic(duration, symmetric_key, fs=8000):
    setup()
    recorded_data = []
    start_time = time.time()
    while (time.time() - start_time) < duration:
        analog_value = read_adc_mic()  # Reading from microphone ADC
        recorded_data.append(analog_value)
        time.sleep(1/fs)

    # Convert ADC readings (integers) to a byte array
    byte_data = np.array(recorded_data, dtype=np.int16).tobytes()
    encrypted_data = encrypt_data(byte_data, symmetric_key)
    return encrypted_data

def record_audio_headphone(duration, symmetric_key, fs=8000):
    setup()
    recorded_data = []
    start_time = time.time()
    while (time.time() - start_time) < duration:
        analog_value = read_adc_headphone()  # Reading from headphone ADC
        recorded_data.append(analog_value)
        time.sleep(1/fs)

    # Convert ADC readings (integers) to a byte array
    byte_data = np.array(recorded_data, dtype=np.int16).tobytes()
    encrypted_data = encrypt_data(byte_data, symmetric_key)
    return encrypted_data

def play_audio_mic(encrypted_data, symmetric_key, fs=8000):
    setup()
    data = decrypt_data(encrypted_data, symmetric_key)

    # Convert decrypted byte array back to integers
    int_data = np.frombuffer(data, dtype=np.int16)

    for value in int_data:
        # Normalize and write to microphone DAC
        write_dac_mic(int(value * 65535 / np.max(np.abs(int_data))))
        time.sleep(1/fs)

def play_audio_headphone(encrypted_data, symmetric_key, fs=8000):
    setup()
    data = decrypt_data(encrypted_data, symmetric_key)

    # Convert decrypted byte array back to integers
    int_data = np.frombuffer(data, dtype=np.int16)

    for value in int_data:
        # Normalize and write to headphone DAC
        write_dac_headphone(int(value * 65535 / np.max(np.abs(int_data))))
        time.sleep(1/fs)

# Example usage for microphone path
if __name__ == "__main__":
    symmetric_key = your_pre_programmed_key_here
    
    duration = 2  # seconds
    fs = 8000  # Sample rate for voice
    print("Recording audio from microphone...")
    encrypted_audio_data_mic = record_audio_mic(duration, fs, symmetric_key)
    print("Playing audio from microphone...")
    play_audio_mic(encrypted_audio_data_mic, fs, symmetric_key)

# Example usage for headphone path
if __name__ == "__main__":
    symmetric_key = your_pre_programmed_key_here
    
    duration = 2  # seconds
    fs = 8000  # Sample rate for voice
    print("Recording audio from headphone...")
    encrypted_audio_data_headphone = record_audio_headphone(duration, fs, symmetric_key)
    print("Playing audio from headphone...")
    play_audio_headphone(encrypted_audio_data_headphone, fs, symmetric_key)