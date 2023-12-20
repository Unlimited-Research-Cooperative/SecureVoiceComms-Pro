import sounddevice as sd

def play_voice(data, fs=44100):
    """
    Play the given voice data.
    :param data: The voice data to play.
    :param fs: Sampling frequency.
    """
    sd.play(data, fs)
    sd.wait()
