import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
def text_to_speech(mytxt):
    language='en'
    voice=gTTS(text=mytxt,lang=language,slow=True)
    voice.save('kilo.mp3')
    playsound('kilo.mp3')
    os.remove('kilo.mp3')

r = sr.Recognizer()
def speech_to_text():

    with sr.Microphone(device_index = 1, sample_rate = 48000,chunk_size = 2048) as source:
         r.adjust_for_ambient_noise(source)
         print("Say Something")
         #listens for the user's input
         audio = r.record(source,duration=3)
                    
         try:
              text = r.recognize_google(audio)
              print("you said: " + text)
              return text 
         except sr.UnknownValueError:
              print("Google Speech Recognition could not understand audio")
         except sr.RequestError as e:
              print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
while True:
    mytext=speech_to_text()
    if mytext:
        mytext=mytext.lower()
        if 'stop' in mytext:
            break
        if 'hi' in  mytext:
            text_to_speech("hello")
        if 'how are you' in mytext:
            text_to_speech("fine how about you")
        
            
            
        
    
