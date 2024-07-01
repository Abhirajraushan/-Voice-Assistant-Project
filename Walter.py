import speech_recognition as sr  #pip install speechrecognition
import pyttsx3  #pip install pyttsx3
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os  #pip install os-sys
import random
import pyautogui  #pip install pyautogui
import youtube_dl  #pip install youtube_dl
import psutil  #pip install psutil


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def screenshot():
    img = pyautogui.screenshot()
    time = datetime.datetime.now().strftime("%d%b%y_%H_%M_%S")
    name = 'D:\\Screenshot' + str(time) + '.png'
    img.save(name)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")   

    else:
        speak("Good Evening!")
        print("Good Evening!")  

    speak("My name is Walter. Please tell me how may I help you")
    print("My name is Walter. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query


if True: 

    Greet()

    while True:    
        query = takeCommand().lower()

        if 'hello' in query or 'hey' in query:
            speak('Hello Sir, How may i help you')

        elif 'your name' in query:
            speak('My name is WALTER')
            print('My name is WALTER')
        
        elif 'wikipedia' in query:            # will search in wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia of ", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("https://www.stackoverflow.com") 
        elif 'open codechef' in query:
            webbrowser.open("https://www.codechef.com/")  

        elif 'cpu' in query:
            usage = str(psutil.cpu_percent())
            speak("CPU usage percent is at"+usage)
            print("CPU usage percent is at: "+usage)
            battery = psutil.sensors_battery()
            speak("battery is at")
            speak(battery.percent)
            print("battery is at: ",battery.percent)

        elif 'play music' in query:
            music_dir = 'D:\\Music'        
            songs = os.listdir(music_dir)
            speak("playing music")    
            os.startfile(os.path.join(music_dir, songs[random.randint(0,3)]))  #randomly play music from the path
 
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%x")    
            speak(f"Sir, the date is {strDate}")
            print(strDate)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%X")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open blackboard' in query:          # will open blackboard
            webbrowser.open("https://cuchd.blackboard.com/ultra/course")

        elif 'open recording' in query:           # will open FAI lecture recordings
            webbrowser.open("https://cumailin-my.sharepoint.com/personal/bb_ece32_cuchd_in/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fbb%5Fece32%5Fcuchd%5Fin%2FDocuments%2F20ECP118%20Foundation%20of%20Artificial%20Intelligence%20Lab&originalPath=aHR0cHM6Ly9jdW1haWxpbi1teS5zaGFyZXBvaW50LmNvbS86ZjovZy9wZXJzb25hbC9iYl9lY2UzMl9jdWNoZF9pbi9Fa3Uta2N0TTZneEN2dDlRQ3BYaFRnVUI0Uk52NlpsX0FsdFNZS3NXWFN2U2RRP3J0aW1lPUpmMVFIVVMwMkVn")
        
        
        elif 'voice' in query:           # will change male voice to female voice
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'search on google' in query:
            speak('What do you want to search for?')
            while True:
                search = takeCommand()
                if search != "None":
                    break
            url = 'https://google.com/search?q=' + search
            webbrowser.open(url)
            speak('Here is What I found for' + search)
        elif 'search on youtube' in query:
            speak('What do you want to search for?')
            while True:
                search = takeCommand()
                if search != "None":
                    break
            url = 'https://www.youtube.com/results?search_query=' + search
            webbrowser.open(url)
            speak('Here is What I found for' + search)
        #All the tasks below will be open in CUIMS...
        elif 'my time table' in query:
            webbrowser.open("https://uims.cuchd.in/UIMS/frmMyTimeTable.aspx")

        elif 'my marksheet' in query:
            webbrowser.open("https://uims.cuchd.in/UIMS/frmStudentMarksView.aspx")

        elif 'my attendance' in query:
            webbrowser.open("https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx?type=etgkYfqBdH1fSfc255iYGw==")

        elif 'home page' in query:
            webbrowser.open("https://uims.cuchd.in/UIMS/StudentHome.aspx")
        
        elif 'quit' in query or 'stop' in query:  # will exit 
            break    #Here code ends....THANK YOU
pytho