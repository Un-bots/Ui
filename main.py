from speech import speak, listen
from ai import ask_ai

def main():

    speak("Hello Sir. Jarvis is now online.")

    while True:

        query = listen()

        if not query:
            continue

        query = query.lower()

        if query in ["exit", "quit", "stop", "goodbye"]:
            speak("Goodbye Sir.")
            break

        if "jarvis" in query:
            query = query.replace("jarvis", "").strip()

            if query == "":
                speak("Yes Sir?")
                continue

        response = ask_ai(query)
        speak(response)

if __name__ == "__main__":
    main()
