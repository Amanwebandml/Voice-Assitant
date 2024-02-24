import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random as rn


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    
    speak("Hello I am Enigma. How can i help you")

def takecommad():
    """it takes microphone commands from the user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print("user said: {query}\n")

    except Exception as e:

        print("say that again please")
        return "None"
    return query



if __name__=="__main__":
    wishMe()
    if 3:
        query = takecommad().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("Accoding to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\Ankit\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[rn.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        