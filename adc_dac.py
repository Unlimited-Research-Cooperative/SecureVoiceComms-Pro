import time
import numpy as np
import busio
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_mcp4725 import MCP4725
import board

# Initialize I2C bus and ADC/DAC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
adc_channel = AnalogIn(ads, ADS.P0)
dac = MCP4725(i2c)

def read_adc():
    return adc_channel.value

def write_dac(value):
    dac.normalized_value = value / 65535

def record_audio(duration, fs=44100):
    recorded_data = []
    start_time = time.time()
    while (time.time() - start_time) < duration:
        analog_value = read_adc()
        recorded_data.append(analog_value)
        time.sleep(1/fs)
    return np.array(recorded_data)

def play_audio(data, fs=44100):
    for value in data:
        write_dac(int(value * 65535))  # Scale the value for the DAC
        time.sleep(1/fs)

# Example usage
if __name__ == "__main__":
    duration = 2  # seconds
    fs = 44100  # Sample rate for audio
    print("Recording audio...")
    audio_data = record_audio(duration, fs)
    print("Playing audio...")
    play_audio(audio_data, fs)
