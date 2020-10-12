import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning to you sir !")
    elif hour>=12 and hour<18:
        speak("good afternoon !")
    else:
        speak("good evening !")
        speak("I an an AI to help you created by Daksh")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeninng.....")
        r.pause_threshold = 1      
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"usar said:{query}\n")
    except Exception as e:
        #print(e)
        print("say again...")
        return "None"
    return query



if _name_ == "_main_" :
    wishMe()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query :
        speak('seraching on wiki..')
        query = query.replace("wikipedia","")  
        results = wikipedia.summary(query,sentences=2)
        speak("from wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'play music' in query:
        music_dir = 'D:\\musicEnglish'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query :
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(strTime)
