import json
from flask import Flask, render_template, request, jsonify   
import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
from ecapture import ecapture as ec


class voiceass:
	def telloutput(self):
		raise NotImplementedError

class open_web_service(voiceass):
    def intro(self):
        speak("web service is now available.")

class google(open_web_service):
    def telloutput(self):
        speak("google is open now.")
    def open(self):
        webbrowser.open_new_tab("https://www.google.com/")

class youtube(open_web_service):
    def telloutput(self):
        speak("youtube is open now.")
    def open(self):
        webbrowser.open_new_tab("https://www.youtube.com")

class github(open_web_service):
    def telloutput(self):
        speak("github is open now.")
    def open(self):
        webbrowser.open_new_tab("https://github.com/")

# class wikipedia(open_web_service):
#     def telloutput(self):
#         speak("wikipedia is open now.")
#     def open(self):
#         webbrowser.open_new_tab("https://github.com/")
    
class gmail(open_web_service):
    def telloutput(self):
        speak("gmail is open now.")
    def open(self):
        webbrowser.open_new_tab("gmail.com")






app = Flask(__name__)

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

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
  

    




    



    
    	    
    return response
    
    
if __name__ == "__main__":

    app.run(debug=True)
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

    while True:
        speak("tell me ,what i can do for you")
        inputcommand = takeCommand().lower()
        if inputcommand==0:
            continue

        

        # a = youtube()
        # a.telloutput() #Prints Woooooof

        if "good bye" in inputcommand or "ok bye" in inputcommand or "stop" in inputcommand:
            speak('your personal voice assestent is shutting down')
            print('your personal voice assestent is shutting down')
            break



        if 'open google' in inputcommand:
            a = google()
            a.open()
            a.telloutput() #Prints Meeeowwwwww
            speak("google is open now")
            time.sleep(2)

        elif 'open youtube' in inputcommand:
            a = youtube()
            a.open()
            a.telloutput()
            
            time.sleep(2)
        elif 'open github' in inputcommand:
            a = github()
            a.open()
            a.telloutput()
            time.sleep(2)
        # elif 'open wikipedia' in inputcommand:
        #     a = wikipedia()
        #     a.open()
        #     a.telloutput()
        #     time.sleep(2)
        elif 'open gmail' in inputcommand:
            a = gmail()
            a.open()
            a.telloutput()
            time.sleep(2)
            
        elif 'professor' in inputcommand:
           
            speak("Dr. Subhajit sidhata is an Assistant Professor with the Department of Electrical Engineering and Computer Science at Indian Institute of Technology, Bhilai working in the area of edge computing, data analytics, distributed systems, and cloud computing.")
            print("Dr. Subhajit sidhata is an Assistant Professor with the Department of Electrical Engineering and Computer Science at Indian Institute of Technology, Bhilai working in the area of edge computing, data analytics, distributed systems, and cloud computing.")
            webbrowser.open_new_tab("https://sites.google.com/iitbhilai.ac.in/subhajit/home")
            time.sleep(2)
        elif 'search'  in inputcommand:
            inputcommand = inputcommand.replace("search", inputcommand)
            webbrowser.open_new_tab(inputcommand)
            time.sleep(2)
        elif 'time' in inputcommand:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in inputcommand:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            time.sleep(2)
       


    time.sleep(2)


    
    
    
