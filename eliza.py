import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Eliza: ", audio)
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Sir how are you feeling today")
    else:
        speak("Good evening")
        speak("had coffee?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Sorry, Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
            
        elif 'open code ' in query:
            codePath = 'A:\\vs code\\Microsoft vs code\\Code.exe'
            os.startfile(codePath)
            
        elif 'digam digam' in query:
           speak("chik chik")
           
        elif 'wasup' in query:
           speak("nothing much ")
           
        elif 'open pornhub' in query:
           speak("It's banned here bruh")
         
        elif 'hello' in query:
           speak("hi how are you!")

       
                       
         
         



