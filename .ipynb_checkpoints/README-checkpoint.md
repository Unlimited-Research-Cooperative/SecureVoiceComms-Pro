markdown

# SecureVoiceComms-Pro

Advanced Encrypted Voice Communication System with Post Quantum Cryptography

## About SecureVoiceComms-Pro

SecureVoiceComms-Pro is an encrypted voice communication system designed for secure and reliable voice transmissions. Leveraging modern encryption techniques, it provides a robust solution for confidential and clear audio communication.

## Features:

- Robust Encryption: Utilizes the NTRU post-quantum cryptographic library to secure communications.
- Audio Processing: Digital signal processing for audio capture and playback.
- File-based Transmission Simulation: Simulates transmission of encrypted voice data through file input/output.
- Python-based: Developed in Python, enabling easy integration and customization.

## Intended Users:

Ideal for users requiring secure communication channels in various domains, including business, remote work, and confidential discussions.

## Use Case Scenarios:

Versatile for scenarios like remote meetings, secure business conversations, and any situation where encrypted voice communication is crucial.

## Hardware Setup:

- Audio Output (Headphone/Speaker): Connect the headphone/speaker pin to a DAC (Digital-to-Analog Converter) on the Raspberry Pi Zero to output decrypted audio signals.
- Audio Input (Microphone): Connect the microphone pin to an ADC (Analog-to-Digital Converter) on the Raspberry Pi Zero to input audio signals.
- Push-to-Talk (PTT) Control: Connect the PTT pin to a GPIO on the Raspberry Pi Zero to control the PTT button simulation.
- Ground Connection: Ensure there is a common ground connection between the Raspberry Pi Zero and the radio.
- ADC/DAC Modules: Connect the ADC (Analog-to-Digital Converter) and DAC (Digital-to-Analog Converter) modules to the Raspberry Pi Zero via the I2C interface.

## Enable I2C Interface:

1. Install Python 3 and PIP:

```bash
sudo apt install python3 python3-pip
```

    Install Adafruit Libraries:
    
```bash
pip3 install adafruit-circuitpython-ads1x15 adafruit-circuitpython-mcp4725
```

    Install Other Required Libraries:

```bash
pip3 install gpiozero
pip3 install numpy
pip3 install cryptography
```

    Install SoundDevice Library:

```bash
pip3 install sounddevice
sudo apt install libportaudio2
```
Running Your Scripts:

Use the following command to run your main.py script:

```bash
python3 main.py
```

Startup Scripts:

You can use a crontab entry or create a systemd service for automatically running your scripts at startup.
Using Crontab:

Edit your crontab file:

```bash
crontab -e
```

Add the following line to the crontab file, replacing /path/to/your/main.py with the full path to your main.py script:

```bash
@reboot python3 /path/to/your/main.py
```

Using Systemd Service:

Create a systemd service file:

```bash

sudo nano /etc/systemd/system/myapp.service
```

Add the following content to the service file, replacing /path/to/your/main.py with the full path to your main.py script:

```bash

[Unit]
Description=My App Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /path/to/your/main.py

[Install]
WantedBy=multi-user.target
```
Enable the service to start on boot:

```bash

sudo systemctl enable myapp.service
```
Start the service:

```bash

sudo systemctl start myapp.service
```
Error Correction/Prevention Modules:

- Frequency Hopping Spread Spectrum (FHSS)
- Error Correction with Convolutional Redundancy and Fail-Safes
- Convolutional Codes with Viterbi Decoding
- Checksums or Cyclic Redundancy Checks (CRC)
- Automatic Repeat Request (ARQ)
- Forward Error Correction (FEC)
- Reed-Solomon Encoding
- Interleaving

To-Do:

- Configure voltage range for ADC/DAC (ADS1115 and MCP4725).
- Ensure that the time.sleep(1/fs) matches the ADC/DAC clock.

Hardware Information:

- ADC Module: ADS1115
- DAC Module: MCP4725




 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Unlimited-Research-Cooperative/SecureVoiceComms-Pro">SecureVoiceComms-Pro</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Synthetic-Intelligence-Labs">Synthetic Intelligence Labs</a> is licensed under <a href="http://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p> 
