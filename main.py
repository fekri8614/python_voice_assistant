import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Function to perform actions based on user input
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "set a reminder" in command:
        speak("What would you like to be reminded of?")
        reminder_text = recognize_speech()
        if reminder_text:
            speak(f"Reminder set: {reminder_text}")
    elif "create a to-do list" in command:
        speak("Sure, please tell me your to-do list.")
        todo_list = recognize_speech()
        if todo_list:
            speak(f"To-do list created: {todo_list}")
    elif "search the web" in command:
        speak("What do you want to search for?")
        search_query = recognize_speech()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
    elif "exit" in command:
        speak("Goodbye!")
        exit()

# Main loop
while True:
    command = recognize_speech()

    if command:
        process_command(command)
