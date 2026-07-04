import google.generativeai as genai
from config import API_KEY

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat History
chat = model.start_chat(history=[])

def ask_ai(prompt):
    """
    Send prompt to Gemini AI and return response.
    """

    try:
        response = chat.send_message(prompt)

        return response.text.strip()

    except Exception as e:
        return f"Sorry Sir, I encountered an error.\n{e}"
