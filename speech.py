import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    """
    Listen to the user's voice and convert it to text.
    """
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You: {text}")
        return text.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""


def speak(text):
    """
    Temporary text output.
    Voice output will be added later.
    """
    print(f"UI: {text}")
