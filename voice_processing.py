import sounddevice as sd
import numpy as np

def record_voice(duration, fs=44100):
    """
    Record voice for a given duration in seconds.
    :param duration: Duration in seconds to record.
    :param fs: Sampling frequency.
    :return: Numpy array of recorded data.
    """
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    return np.squeeze(recording)  # Remove channel axis
