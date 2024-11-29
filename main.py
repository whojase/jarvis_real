import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
import os

from comands_jarvis import com

r = sr.Recognizer()
m = sr.Microphone()

sr.LANGUAGE = 'ru-RU'

engine = pyttsx3.init()

print("Запись пошла, говорите. Чтобы завершить, скажите 'стоп'.")

while True:
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Слушаю... Говорите!")

        audio = r.listen(source, timeout=None, phrase_time_limit=None)
        
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(f'Вы сказали: {text.lower()}')

        if text.lower() in com['alies']:
            engine.say("Привет, как я могу помочь?")
            engine.runAndWait()

        elif text.lower() in com['time']:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M")
            engine.say('Выполняю сэр.')
            time.sleep(1)
            engine.say(f"Текущее время: {current_time}")
            engine.runAndWait()

        elif text.lower() in com['bye']:
            engine.say("До свидания!")
            engine.runAndWait()
            break

        elif text.lower() in com['help']:
            engine.say(f'Я голосовой помощник со встроеным искуственым интелектом разработаный тони страком. У меня есть множество функций, от обычного открывания програм - до диогностики системы')
            engine.runAndWait()
        
        elif text.lower() in com['open_browser']:
            engine.say('Секунду, выполняю сэр')
            time.sleep(1)
            engine.say("Открываю браузер.")
            engine.runAndWait()
            webbrowser.open('https://www.google.com')
        
        elif text.lower() in com['open_explorer']:
            engine.say('Выполняю, сэр')
            time.sleep(1)
            engine.say("Открываю проводник.")
            engine.runAndWait()
            os.system('explorer')
        
        elif text.lower() in com['open_youtube']:
            engine.say('Секунду, выполняю сэр')
            time.sleep(1)
            engine.say("Открываю ютуб.")
            engine.runAndWait()
            webbrowser.open('https://www.youtube.com')
        
        elif text.lower() in com['open_vk']:
            engine.say('Секунду, выполняю сэр')
            time.sleep(1)
            engine.say("Открываю вконтакте.")
            engine.runAndWait()
            webbrowser.open('https://www.vk.ru')

        elif text.lower() in com['open_funpay']:
            engine.say('Секунду, выполняю сэр')
            time.sleep(1)
            engine.say("Открываю funpay.")
            engine.runAndWait()
            webbrowser.open('https://www.funpay.com')

    except sr.UnknownValueError:
        print("Не удалось распознать речь, повторите.")
    except sr.RequestError:
        print("Ошибка соединения с сервисом Google. Попробуйте позже.")