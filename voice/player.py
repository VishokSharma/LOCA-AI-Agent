import time
import pygame


class AudioPlayer:

    def __init__(self):

        pygame.mixer.init()

    def play(
        self,
        audio_file: str
    ):

        pygame.mixer.music.load(
