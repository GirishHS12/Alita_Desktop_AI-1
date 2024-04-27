import re

from playsound import playsound
import eel
import os
from engine.command import speak, takecommand
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import time
import pyautogui

# playing assistant sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def play_youtube(query):
    speak("What would you like to play ?")
    song_query = takecommand()
    #search_term=extract_yt_term(song_query)
    speak(f"Playing {song_query} on YouTube")
    kit.playonyt(song_query)
    #time.sleep(2)
    pyautogui.hotkey('f')

def extract_yt_term(command):
    #Define a regular expression pattern a capture the song name
    pattern = command
    #use re.search to find the match in the command
    match=re.search(pattern,command,re.IGNORECASE)
    #If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else didntGetRes()

def didntGetRes(command):
    query=takecommand()
    play_youtube(query)

def openCommand(query):
    query.lower()
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    
    if query!="":
        speak("Opening "+query)
        os.system('start '+query)

        
    else:
        speak("not found")