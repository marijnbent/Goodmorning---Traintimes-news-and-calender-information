import subprocess
import arrow
from textblob import TextBlob
from gtts import gTTS
import google_calender

calender_id = "j6mj17sc6ve48asaijtr212jt0@group.calendar.google.com"

def SpeakSentence (string):
    audio_file = "temp.mp3"
    tts = gTTS(text=string, lang="nl")
    tts.save(audio_file)
    return_code = subprocess.call(["afplay", audio_file])

def Translate (string):
    b = TextBlob(string)
    b = str(b.translate(to="nl"))
    return b

next_class = google_calender.main(calender_id)
print (next_class)
print (next_class[1])

date = str(arrow.utcnow().format('dddd DD MMMM', locale='nl'))
time = str(arrow.utcnow().format('H:m'))
text = "Goedemorgen Marijn. Het is nu " + date + " en " + time
SpeakSentence(text)


text = "Je hebt de les " + next_class[1] + "over 1 uur"
SpeakSentence(text)



