from gtts import gTTS
from playsound import playsound
import os
def text_to_speech(mytxt):
    language='en'
    voice=gTTS(text=mytxt,lang=language,slow=True)
    voice.save('kilo.mp3')
    playsound('kilo.mp3')
    os.remove('kilo.mp3')
text_to_speech("Kilowatt")
text_to_speech("Per metre Cube")
