import subprocess
import arrow
from textblob import TextBlob
from gtts import gTTS

def SpeakSentence (string):
    audio_file = "temp.mp3"
    tts = gTTS(text=string, lang="nl")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])

def Translate (string):
    b = TextBlob(string)
    b = str(b.translate(to="nl"))
    return b

date = str(arrow.utcnow().format('dddd DD MMMM'))
date = Translate(date)
time = str(arrow.utcnow().format('H:m'))
text = "Goedemorgen Marijn. Het is nu " + date + " en " + time

SpeakSentence(text)


