import tempfile
import time

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

from voice.config import (
    SAMPLE_RATE,
    CHANNELS,
    CHUNK_SIZE,
    SILENCE_THRESHOLD,
    SILENCE_DURATION,
    MIN_RECORD_SECONDS,
    MAX_RECORD_SECONDS
)


class Recorder:

    def __init__(self):

        self.recording = False

        self.audio = []

    def record(self):

        input("\nPress ENTER to start recording...")

        print("\n🎤 Recording...")
        self.recording = True

