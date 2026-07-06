import os

from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()


class SpeechToText:

    def __init__(self):

        self.client = DeepgramClient(
            api_key=os.getenv("DEEPGRAM_API_KEY")
        )

