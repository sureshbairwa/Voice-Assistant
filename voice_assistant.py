
import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
from ecapture import ecapture as ec


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Sir, Welcome to Principle of programing languages CS300 course ")
        print("Hello,Good Morning Sir, Welcome to Principle of programing languages CS300 course")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon  Sir, Welcome to Principle of programing languages CS300 course")
        print("Hello,Good Afternoon Sir, Welcome to Principle of programing languages CS300 course")
    else:
        speak("Hello,Good Evening  Sir, Welcome to Principle of programing languages CS300 course")
        print("Hello,Good Evening Sir, Welcome to Principle of programing languages CS300 course")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening voice")
        audio=r.listen(source)

        try:
            inputcommand=r.recognize_google(audio,language='en-in')
            print(f"user said:{inputcommand}\n")

        except Exception as e:
            speak("Please say again")
            return "None"
        return inputcommand

# speak("")
wishMe()


if __name__=='__main__':


    while True:
        speak("tell me ,what i can do for you")
        inputcommand = takeCommand().lower()
        if inputcommand==0:
            continue

        if "good bye" in inputcommand or "ok bye" in inputcommand or "stop" in inputcommand:
            speak('your personal voice assestent is shutting down')
            print('your personal voice assestent is shutting down')
            break



        if 'open google' in inputcommand:
            webbrowser.open_new_tab("https://www.google.com/")
            speak("google is open now")
            time.sleep(5)
            
        elif 'professor' in inputcommand:
           
            speak("Dr. Subhajit sidhata is an Assistant Professor with the Department of Electrical Engineering and Computer Science at Indian Institute of Technology, Bhilai working in the area of edge computing, data analytics, distributed systems, and cloud computing.")
            webbrowser.open_new_tab("https://sites.google.com/iitbhilai.ac.in/subhajit/home")
            time.sleep(5)
       


time.sleep(3)











