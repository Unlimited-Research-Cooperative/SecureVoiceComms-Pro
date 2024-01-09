SecureVoiceComms-Pro

Advanced Encrypted Voice Communication System

About SecureVoiceComms-Pro

SecureVoiceComms-Pro is an encrypted voice communication system designed for secure and reliable voice transmissions. Leveraging modern encryption techniques, it provides a robust solution for confidential and clear audio communication.

🌐 Features:

- Robust Encryption: Uses standard cryptographic libraries to secure communications.
- Audio Processing: Digital signal processing for audio capture and playback.
- File-based Transmission Simulation: Simulates transmission of encrypted voice data through file input/output.
- Python-based: Developed in Python, enabling easy integration and customization.

🛠 Intended Users
Ideal for users requiring secure communication channels in various domains, including business, remote work, and confidential discussions.

📡 Use Case Scenarios
Versatile for scenarios like remote meetings, secure business conversations, and any situation where encrypted voice communication is crucial.

🔧 Contribution & Collaboration
Contributions from experts in cryptography, audio processing, and software development are welcome to enhance and refine SecureVoiceComms-Pro.

Setup and Usage

To use SecureVoiceComms-Pro, follow these steps:
- Environment Setup: Ensure Python and necessary libraries (sounddevice, numpy, cryptography) are installed.
- Recording Audio: Use the microphone for audio input. The system captures and processes this audio.
- Encryption Key: Define a secure encryption key. Replace b'your-encryption-key-32bytes' in the script with a 32-byte key for AES-256 encryption.
- Testing the Code: Execute test.ipynb to start the recording, encryption, simulated transmission, decryption, and playback process.
- Output: The decrypted audio is saved as a .wav file, which can be played back to verify the process.

Note
Ensure your encryption key is stored and handled securely. The current implementation is a basic model and should be further adapted for specific operational environments.




Work In Progress Notes:

Hardware:

    Audio Output (Speaker):
        Connect the speaker pin to a DAC (Digital-to-Analog Converter) on the Raspberry Pi Zero to output decrypted audio signals to the radio.

    Audio Input (Microphone):
        Connect the microphone pin to an ADC (Analog-to-Digital Converter) on the Raspberry Pi Zero to input audio signals from the radio for encryption.

    PTT Control:
        Connect the PTT pin to a GPIO on the Raspberry Pi Zero. You will control this GPIO within your software to simulate pressing the PTT button. When the GPIO is set to low, it should trigger the PTT.

    Ground Connection:
        Ensure there is a common ground connection between the Raspberry Pi Zero and the radio.
        
    Connect the ADC and DAC modules to the Raspberry Pi Zero via the I2C interface.

Enable I2C Interface

Install Python 3 and PIP
sudo apt install python3 python3-pip

Install Adafruit Libraries:
pip3 install adafruit-circuitpython-ads1x15 adafruit-circuitpython-mcp4725

Install Other Required Libraries:
pip3 install gpiozero

pip3 install numpy
pip3 install cryptography

Install SoundDevice Library:
pip3 install sounddevice

sudo apt install libportaudio2


SCP, FTP, or by directly writing the files on the Raspberry Pi using a text editor
Libraries to install 
Run Your Scripts:
python3 main.py

use a crontab entry or create a systemd service
crontab -e


@reboot python3 /path/to/your/main.py # Replace /path/to/your/main.py with the full path to your main.py script


Using Systemd Service:
sudo nano /etc/systemd/system/myapp.service

Add the following content to the service file:
[Unit]
Description=My App Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /path/to/your/main.py # Replace /path/to/your/main.py with the full path to your main.py script

[Install]
WantedBy=multi-user.target

Enable the service to start on boot:
sudo systemctl enable myapp.service

Start the service:
sudo systemctl start myapp.service


possible error correction/prevention modules:

Frequency Hopping Spread Spectrum (FHSS)
Error Correction with Convolutional 
Redundancy and Fail-Safes
Convolutional Codes with Viterbi Decoding
Checksums or Cyclic Redundancy Checks (CRC)
Automatic Repeat Request (ARQ)
Forward Error Correction (FEC)
Reed-Solomon Encoding
Interleaving


todo:
adc_dac.py: voltage range of adc/dac?
time.sleep(1/fs): match adc/dac clock

adc: ADS1115
dac: MCP4725



 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Unlimited-Research-Cooperative/SecureVoiceComms-Pro">SecureVoiceComms-Pro</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Synthetic-Intelligence-Labs">Synthetic Intelligence Labs</a> is licensed under <a href="http://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p> 
