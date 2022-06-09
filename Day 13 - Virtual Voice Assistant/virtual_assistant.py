import pyttsx3 as ptsx
# import pywhatkit as pwk
# import yfinance as yf
# import pyjokes as pj
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
from datetime import date, datetime

LANG = 'es-ES'
# LANG = 'ca'

id_es_es_1 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id_en_us_1 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id_en_us_2 = "id=HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# calendar = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
#            3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
calendar = {0: "Lunes", 1: "Martes", 2: "Miércoles",
            3: "Jueves", 4: "Viernes", 5: "Sabado", 6: "Domingo"}


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


def display_voices():
    engine = ptsx.init()
    for voice in engine.getProperty('voices'):
        print(voice)


def get_day():
    today = date.today()
    day = calendar.get(today.weekday())
    return f"Hoy es {day}"


def get_hour():
    hour = datetime.now().hour
    minutes = datetime.now().minute
    return f"Son las {hour} y {minutes}"


def open_link(link):
    webbrowser.open(link)


def tell_greetings():
    transform_text2audio("Hola, bienvenido a tu asistente virtual.")


def tell_goodbye():
    transform_text2audio("Ha sido un placer. Hasta pronto!")


def start_assistant():
    ask = True
    tell_greetings()
    while ask:
        request = ""
        request = transform_audio2text().lower()
        print(request)
        if 'salir' in request:
            tell_goodbye()
            ask = False
        elif 'abrir youtube' in request:
            transform_text2audio("Abriendo youtube!")
            open_link("https://www.youtube.com")
        elif 'abrir navegador' in request:
            transform_text2audio("Vamos a abrir tu navegador")
            webbrowser.open('https://www.google.es')
        elif 'qué día es' or 'en qué día estamos' in request:
            transform_text2audio(get_day())
        elif 'qué hora es' in request:
            transform_text2audio(get_hour())
        elif 'busca en wikipedia' in request:
            request = request.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            result = wikipedia.summary(request, sentences=1)
            transform_text2audio(f"Wikipedia dice esto sobre {request}: {result}")


start_assistant()
# transform_text2audio(transform_audio2text())
# display_voices()
# tell_day()
# tell_hour()
