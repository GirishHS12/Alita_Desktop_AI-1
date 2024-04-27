import time
import pyautogui
import pyaudio
import pvporcupine
import struct
import os

keyword_path='www\\assets\\alita keyword\\alita_en_windows_v3_0_0.ppn'
porcupine = None
keyword=['alita']

try:
    porcupine=pvporcupine.create(keyword_keywords=keyword,keyword_paths=[os.path.join(keyword_path,'www\\assets\\alita keyword\\alita_en_windows_v3_0_0.ppn')])
except  pvporcupine.PorcupineException as e:
    print(f"failed to create porcupine:{e}")

def hotword():

    porcupine=None
    paud=None
    audio_stream=None
    
    try:
        #pre Trained keywords
        porcupine=pvporcupine.create(access_key='${6R+qJMqUy7Pfv8aw5oPkMMroE4WTExVGQRnkUGWpL1ByXQ5BCgxpXw==}',keyword=['${www\\assets\\alita keyword\\alita_en_windows_v3_0_0.ppn}'])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        #loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            
            #processing keyword comes mic
            keyword_index=porcupine.process(keyword)
            
            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                
                #pressing shortcut key win+j
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

hotword()