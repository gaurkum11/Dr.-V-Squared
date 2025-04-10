#step1 : setup audio recorder(ffmeg & portaudio)
import os

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s -%(message)s')

def record_audio(file_path, timeout=20,phrase_time_limit=None):
    """
    Simplified function to record audi from microphone and save it as an MP3 file.

    Args:
    file_path (str) : Path to save the recorded audio file.
    timeout (int) : Maximum time to wait for a phrase to start ( in seconds).
    phrase_time_lfimit (int) : maximum time for the phrase to be recorded (in seconds).
    """

    recognizer = sr.Recognizer()

    try :
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise")
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            logging.info("Start speaking now...")

            #record audio
            audio_data = recognizer.listen(source,timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # convert recorded audio to mp3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path,format="mp3",bitrate="128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"and error occured: {e}")

audio_file_path="patient_voice_test.mp3"
record_audio(file_path=audio_file_path)


#step2 : setup speech to text-STT-model for transcription
#openai whisper model speech to text 

from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

stt_model = "whisper-large-v3-turbo"
def transcribe_with_groq(stt_model, audio_file_path,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file = audio_file,
        language="en"
    )
    return transcription.text




