from speech import listen, speak
from ai import ask_ai
from config import ASSISTANT_NAME

def main():
    speak(f"{ASSISTANT_NAME} is now online.")

    while True:
        query = listen()

        if not query:
            continue

        if query in ["exit", "quit", "stop", "goodbye"]:
            speak("Goodbye Sir.")
            break

        response = ask_ai(query)
        speak(response)

if __name__ == "__main__":
    main()
