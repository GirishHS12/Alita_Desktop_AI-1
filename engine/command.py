import pyttsx3
import speech_recognition as sr
import datetime
import eel
import os
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',190)


#This is a speak Fun() where Alita is able to speak'''
def speak(audio):

    engine.say(audio)
    eel.DisplayMessage(audio)
    #print(audio)
    engine.runAndWait()
    
@eel.expose   
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\rListening...")
        eel.DisplayMessage('\rListening...')
        r.pause_threshold = 1
        audio = r.listen(source,10,6)

    try:
        print("\rRecognizing...")
        eel.DisplayMessage('\rRecognizing...')
        query = r.recognize_google(audio,language='en-in')
        eel.DisplayMessage(query)
        #time.sleep(2)
        speak(query)
        #eel.ShowHood()

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

@eel.expose
def wish():
    hour=int(datetime.datetime.now().hour)

    if(hour>=0 and hour<=12):
        speak("Good Morning Master")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon Master")
    else:
        speak("Good Evening Master")

    speak("Im Alita...Your Personal AI Assistant...Please tell me How can I help you")

#if __name__ == "__main__":

#takecommand()
#speak("Hi....Im Alita....Your Personal AI Assistant...How can I help you")
# wish()
# query=takecommand()
 #speak(query)

@eel.expose
def allCommand():
    
    try:
        query=takecommand()
        print(query)

        if "open youtube" in query.lower():
          from engine.features import play_youtube
          play_youtube(query)
        
        elif "open" in query.lower():
           from engine.features import openCommand
           openCommand(query)
        else:
            print("not run")
    except:  
        
        print("Error")
    
        
    eel.ShowHood()