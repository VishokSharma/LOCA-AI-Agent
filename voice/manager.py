import os

from voice.recorder import Recorder
from voice.stt import SpeechToText
from voice.tts import TextToSpeech
from voice.player import AudioPlayer


class VoiceManager:

    def __init__(self):

        self.recorder = Recorder()

        self.stt = SpeechToText()

        self.tts = TextToSpeech()
