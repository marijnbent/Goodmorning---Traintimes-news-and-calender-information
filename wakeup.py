import subprocess
import arrow
import requests
import datetime
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

#Saying goodmorning
date = str(arrow.utcnow().format('dddd DD MMMM', locale='nl'))
time = str(arrow.utcnow().format('H:m'))
text = "Goedemorgen Marijn. Het is nu " + date + " en " + time
SpeakSentence(text)

#Give me my next class details
next_class = google_calender.main(calender_id)
t1 = datetime.datetime.strptime(next_class[0], '%Y-%m-%dT%H:%M:%S+01:00')
if (t1.minute == 0):
    text = "Je hebt de les " + next_class[1] + "om" +  str(t1.hour) + "uur"
else:
    text = "Je hebt de les " + next_class[1] + "om" +  str(t1.hour) + "uur" + str(t1.minute)
SpeakSentence(text)

#When do I need to leave?
arrival_time = next_class[0].replace("00+01:00", "")
arrival_time = arrival_time.replace(":", "")
url = "https://api.9292.nl/0.1/journeys?before=1&sequence=1&byFerry=false&bySubway=true&byBus=false&byTram=false&byTrain=true&lang=nl-NL&from=station-hilversum-sportpark&dateTime=" + arrival_time + "&searchType=arrival&interchangeTime=standard&after=1&to=rotterdam_metrostation-beurs"
r = requests.get(url).json()
departure = datetime.datetime.strptime(r['journeys'][1]['departure'], '%Y-%m-%dT%H:%M')
# departure_from_home = datetime.datetime.strptime(departure.timestamp() - 1200, %H:%M:%S)

text = "Je trein vertrekt om " + str(departure.hour) + " uur " + str(departure.minute) + "."
SpeakSentence(text)



