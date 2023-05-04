import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("t.ogg", "rb")
tr = openai.Audio.transcribe("whisper-1", audio_file)
print(tr)
