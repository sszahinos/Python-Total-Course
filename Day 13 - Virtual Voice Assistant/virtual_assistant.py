"""import pyttsx3 as ptsx
import pywhatkit as pwk
import yfinance as yf
import pyjokes as pj
import webbrowser
import datetime
import wikipedia"""
import speech_recognition as sr
import pyaudio

LANG = 'es-ES'


# audio -> text
def transform_audio_text():
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


transform_audio_text()
