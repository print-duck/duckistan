from gtts import gTTS
from playsound import playsound

mytxt='Hello'
language='en'
voice=gTTS(text=mytxt,lang=language,slow=True)
voice.save('kilo.mp3')
playsound('kilo.mp3')

