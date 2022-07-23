import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')  # sapi5 is use to take voices
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am jarvis, please tell me how may i help you")

def TakeCommand():
    '''this function takes my command
    it takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='hindi-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "none"

    return query


if __name__ == '__main__':
    # speak("hello sir. How may i help you")
    wishme()
    while True:
        query=TakeCommand().lower()
     # logic for executing task
        if 'wikipedia' in query :
            speak('searching..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
          webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("chrome")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open code with harry' in query:
            webbrowser.open("codewithaharry.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            webbrowser.open("Twitter.com")

        elif 'play music' in query:
            path = 'E:\songs'
            file = os.listdir(path)
            print(file)
            a=random.choice(file)
            os.startfile(os.path.join(path,file[0]))
            # path = "E:\songs"
            # mixer.init()
            # mixer.music.load(path)
            # mixer.music.play()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"time is {strTime}")
