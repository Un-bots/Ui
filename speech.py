import subprocess
import os

def speak(text):
    print(f"Jarvis: {text}")
    os.system(f'termux-tts-speak "{text}"')

def listen():
    print("Listening... Speak after the beep.")

    subprocess.run([
        "termux-microphone-record",
        "-f",
        "/sdcard/jarvis.wav",
        "-l",
        "5"
    ])

    return input("You: ")
