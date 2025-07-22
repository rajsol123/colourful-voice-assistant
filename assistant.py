import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            speak("Sorry, I didn't catch that.")
            return ""

def handle_query(query):
    if 'time' in query:
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")
        return f"Time is {time}"
    
    elif 'youtube' in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
        return "Opened YouTube"

    elif 'google' in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")
        return "Opened Google"

    elif 'exit' in query or 'quit' in query:
        speak("Goodbye!")
        return "Goodbye"

    else:
        speak("Sorry, I can't do that yet.")
        return "Command not recognized"
