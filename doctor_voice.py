#Step1a: Setup text tp speech-TTS-model (with gTTSs)

import os
from gtts import gTTS


import subprocess
import platform
from playsound import playsound

def text_to_speech_wth_gtts_old(input_text, output_file_path):
    language = "en"
    audio_obj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_obj.save(output_file_path)

input_text="Hi This is gaurav kumar from fnm"
#text_to_speech_wth_gtts_old(input_text=input_text,output_file_path="gtt_testing.mp3")


#Step1b: Setup text tp speech-TTS-model (with Elevenlabs)
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_elevenlab_old(input_text,output_file_path):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_file_path)

#text_to_speech_with_elevenlab_old(input_text=input_text, output_file_path= "elevenlab_testing.mp3")

#step2: use model for text output to voice

import time


def text_to_speech_wth_gtts(input_text, output_file_path):
    language = "en"
    audio_obj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_obj.save(output_file_path)
    os_name = platform.system()

    try:
        if os_name == "Darwin": #macOS
            subprocess.run(['afplay',output_file_path])
        elif os_name == "Windows": # windows
            playsound(output_file_path)
            time.sleep(1)
            #os.environ(output_file_path)
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_file_path}").PlaySync();'])
        elif os_name == "Linux": #Linux
            subprocess.run(['aplay',output_file_path]) 
        else: 
            raise OSError("Unsupporetd OS")
    except Exception as e:
        print(f"An error occured while trying to play the audio: {e}")


input_text="Hi playing audio using elevenlabs autoplay"
#text_to_speech_wth_gtts(input_text=input_text,output_file_path="gtt_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_file_path):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_file_path)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_file_path])
        elif os_name == "Windows":  # Windows
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_file_path}").PlaySync();'])
            playsound(output_file_path)
            time.sleep(1)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_file_path])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#text_to_speech_with_elevenlabs(input_text, output_file_path="elevenlabs_testing_autoplay.mp3")
