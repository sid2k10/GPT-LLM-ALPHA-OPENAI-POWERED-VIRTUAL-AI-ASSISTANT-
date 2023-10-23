# Import necessary libraries and modules
import datetime
import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import random
import openai
import wmi
from datetime import datetime, date
from coinfig import apikey  # Assuming this is your API key for OpenAI

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Get available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Adjust speech rate (optional)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 300)  # Decrease rate by 50 (adjust as needed)

# Adjust volume (optional)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume + 0.25)  # Increase volume by 0.25 (adjust as needed)

# Set OpenAI API key
openai.api_key = apikey

# Initialize chat history
chatSTR = ""

# Define a function for interactive chat with OpenAI
def chat(query):
    global chatSTR
    chatSTR += f"sid: {query}\n Alpha: {query}\n"
    
    # Send the query to OpenAI and receive a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatSTR,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Speak the response and print it
    speak(response["choices"][0]["text"])
    print(response["choices"][0]["text"])
    
    # Save the conversation to a file (optional)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f'Openai/prompt - {random.randint(1, 2342342324234)}', "w") as f:
        f.write(text)

# Define a function for AI responses to specific prompts
def ai(prompt):
    text = f"OpenAI response for prompt: {prompt}\n********************\n\n"
    
    # Send the prompt to OpenAI and receive a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Print the response and speak it
    print(response["choices"][0]["text"])
    speak(response["choices"][0]["text"])
    
    # Save the response to a file (optional)
    if not os.exists("Openai"):
        os.mkdir("Openai")
    with open(f'Openai/prompt - {random.randint(1, 2342342324234)}', "w") as f:
        f.write(text)

# Define a function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define a function to capture voice commands
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1

        # Listen for voice input
        audio = r.listen(source)
        try:
            # Recognize and print user's query
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Alpha"

if __name__ == "__main__":
    print("Welcome")
    speak("Jai Bajrang Bali")
    speak("I am Alpha. I am here to help you. Ask me anything.")
    speak("What can I do for you?")
    
    while True:
        print("Listening...")
        query = take_command()
        
        # Perform various actions based on user queries
        if "open Google and search" in query:
            search_query = query.split("open Google and search")[1].strip()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speak(f"Searching {search_query} on Google...")

        sites = [["YouTube", "https://www.youtube.com/"],
                 ["Wikipedia", "https://www.wikipedia.org/"],
                 ["Google", "https://www.google.com/?authuser=0"]]

        for site in sites:
            if f"open {site[0].lower()}" in query.lower():
                webbrowser.open(site[1])
                speak(f"Opening {site[0]} sir...")

        apps = [["VS Code", "D:\\Microsoft VS Code\\Code.exe"],
                ["Brave", "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"]]

        for app in apps:
            if f"open {app[0].lower()}" in query.lower():
                os.startfile(app[1])
                speak(f"Opening {app[0]} sir...")

        elif "the time" in query:
            strfTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strfTime}")

        elif "the date" in query:
            today = date.today()
            speak(f"Sir, today is {today}")

        elif "help me " in query.lower():
            ai(prompt=query)

# The main section of the code listens to user queries, interprets them, and responds accordingly.
