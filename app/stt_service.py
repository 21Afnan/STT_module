import os
import tempfile
from openai import OpenAI
from .config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def transcribe_audio_file(file_bytes: bytes, filename: str) -> str:
    """Transcribes an audio file using OpenAI Whisper."""
    suffix = os.path.splitext(filename)[1] or ".webm"
    tmp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        with open(tmp_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript.text

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
