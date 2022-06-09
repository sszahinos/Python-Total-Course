import pyttsx3 as ptsx
"""import pywhatkit as pwk
import yfinance as yf
import pyjokes as pj
import webbrowser
import datetime
import wikipedia"""
import speech_recognition as sr

LANG = 'es-ES'
#LANG = 'ca'

id_es_es_1 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id_en_us_1 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id_en_us_2 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"


# audio -> text
def transform_audio2text():
    # Initializing recognizer
    rec = sr.Recognizer()

    # Micro config
    with sr.Microphone() as origin:
        # waiting time
        rec.pause_threshold = 0.8

        # tell that the record has begun
        print("You can talk now.")

        # Save audio
        audio = rec.listen(origin)

        try:
            # search in google
            request = rec.recognize_google(audio, language=LANG)

            # print transformed audio to text
            print("You said: " + request)

            return request
        except sr.UnknownValueError:  # Don't understanding the audio
            print("I didn't understand you.")
            return "I keep waiting"
        except sr.RequestError:  # Request no resolved
            print("I can't resolve the request.")
            return "I keep waiting"
        except:
            print("Unexpected error")
            return "I keep waiting"

def transform_text2audio(message):
    engine = ptsx.init()
    engine.setProperty('voice', id_es_es_1)

    # speak
    engine.say(message)
    engine.runAndWait()

transform_text2audio(transform_audio2text())
"""
engine = ptsx.init()
for voice in engine.getProperty('voices'):
    print(voice)
"""

