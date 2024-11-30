import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
import os
import pyautogui
from playsound import playsound

from comands_jarvis import com
from app.play_sound import play_sound

# Настройки речевого движка
def speak(text):
    """Озвучивает текст с использованием pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Настройки микрофона
r = sr.Recognizer()
m = sr.Microphone()

sr.LANGUAGE = 'ru-RU'


while True:
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Слушаю... Говорите!")
        audio = r.listen(source, timeout=None, phrase_time_limit=None)
        
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(f'Вы сказали: {text.lower()}')

        # Реакция на команды
        if text.lower() in com['alies']:
            play_sound('sounds\hello.wav')

        elif text.lower() in com['bye']:
            break

        elif text.lower() in com['open_browser']:
            webbrowser.open('https://www.google.com')
            play_sound('sounds\comfirm.wav')

        elif text.lower() in com['open_explorer']:
            os.system('explorer')
            play_sound('sounds/always_at_your_service.wav')

        elif text.lower() in com['open_youtube']:
            play_sound('sounds/loading.wav')
            webbrowser.open('https://www.youtube.com')

        elif text.lower() in com['open_vk']:
            play_sound('sounds/no_problem.wav')
            webbrowser.open('https://www.vk.ru')

        elif text.lower() in com['open_funpay']:
            play_sound('sounds/always.wav')
            webbrowser.open('https://www.funpay.com')

        elif text.lower() in com['shutdown']:
            play_sound('sounds/off.wav')
            os.system('shutdown /s /t 1')
        

        else:
            # Ответ на неизвестную команду
            response = "Извините, я не понял вашу команду."
            speak(response)

    except sr.UnknownValueError:
        response = "Не удалось распознать речь, повторите."
        print(response)
        speak(response)

    except sr.RequestError:
        response = "Ошибка соединения с сервисом Google. Попробуйте позже."
        print(response)
        speak(response)
