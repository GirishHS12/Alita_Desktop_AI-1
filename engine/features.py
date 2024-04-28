from playsound import playsound
import eel
import os
from engine.command import speak, takecommand
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import time
import pyautogui
import pyaudio
import pvporcupine
import struct

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

def hotword():
    
    porcupine = None
    paud = None
    audio_stream = None
    try:

        # pre trained keywords
        porcupine = pvporcupine.create(access_key='6R+qJMqUy7Pfv8aw5oPkMMroE4WTExVGQRnkUGWpL1ByXQ5BCgxpXw==',keyword_paths=['C:\\Users\Girish\OneDrive\Desktop\Alita-AI\Alita AI\www\\assets\\alita keyword\\alita_en_windows_v3_0_0.ppn'])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True,
                                 frames_per_buffer=porcupine.frame_length)

        # loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # processing keyword comes from mic
            keyword_index = porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index >= 0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


def openCommand(query):
    query.lower()
    query=query.replace(ASSISTANT_NAME,"")
    query=query.replace("open","")
    
    if query!="":
        speak("Opening "+query)
        os.system('start '+query)

        
    else:
        speak("not found")