import speech_recognition as sr # чтобы записывать голос и переводить его в текст
import pyttsx3 # это нужно, чтобы возможно было озвучивать текст
import subprocess
from random import randint
import pygame
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from keyboard import is_pressed
from keyboard import send
from mutagen.mp3 import MP3
from math import ceil
from tqdm import tqdm


start = pyttsx3.init()

def my_music(): # надо добавить способ ставить на паузу или выйти из музыки
    music_list = ['DJ Smash feat. Poet - Беги (megapesni.com).mp3',
                  'm_dee_-_naivnaya_(feat._abdr.__the_limba)_stopmusic.net.mp3',
                  'jah_khalib_-_sunshine_lady_(z2.fm).mp3', 'MiyaGi & Andy Panda - Kosandra.mp3',
                  'jah-khalib_-_kolybelnaya.mp3', '17631-raim-baila.mp3', '17633-raim-where-are-you.mp3']
    music_choice = randint(0, len(music_list) - 1)
    music_played = music_list[music_choice]
    pygame.init()
    text_before_music = 'включаю вашу музыку'
    start.say(text_before_music)
    start.runAndWait()
    f = MP3(fr'C:\Users\Admin\Desktop\Rasul\Music\{music_played}')
    len_music = ceil(f.info.length)
    print(len_music)
    # Вот здесь надо определить продолжительность музыки, поставить таймер и по окончании имитировать нажатие клавиш
    # 2 Поставить таймер
    # 3 Имитировать нажатие клавиш
    song = pygame.mixer.Sound(fr'C:\Users\Admin\Desktop\Rasul\Music\{music_played}')
    clock = pygame.time.Clock()

    song.play()
    n = 0
    list_for_time_music = [0 for i in range(len_music)]
    # stop_signal = listen()
    # есть идея: поставить внутри while Microphone и песня продолжить while m != 'отключи музыку' or 'все хватит' m = listen()
    stop_keyboard = is_pressed('ctrl+alt+i')
    while n <= len_music and not stop_keyboard:
        for i in tqdm(range(len_music)):
            sleep(1)
        # stop_signal = listen()
        ostalos_ = len_music - n
        min_uta = ostalos_ // 60
        sec_unda = ostalos_ % 60
        # print(f'музыка продолжается {n} секунд\nосталось {min_uta} минут, {sec_unda} секунд')
        # надо минуту добавить //60 и % 60
        sleep(1)
        n += 1
        # clock.tick(60)
    pygame.quit()

def listen():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)

            try:
                task = r.recognize_google(audio, language='ru-RU').lower()
                print(task)
            except:
                task = listen()
            return task
def request(task):
    if 'пока' in task:
        text = 'всего доброго хозяин'
        start.say(text)
        start.runAndWait()
    elif 'сара' in task or 'sarah' in task or 'сара ты здесь' in task or 'помощница' in task or 'где ты искусственный интеллект' in task or 'zara' in task or 'шарарам' in task:
        names = ["Расул", "Расул Ислямгали"]
        replica_ = ['чего желаете?', 'что мне включить?', 'хотите музыку?', "как тебе такое Илон Маск?"]
        name_choice = randint(0, 1)
        replica_choice = randint(0, 3)
        welcome_text = f'Приветствую вас {names[name_choice]}, {replica_[replica_choice]}'
        print(welcome_text)
        start.say(welcome_text)
        start.runAndWait()

    elif 'музыка' in task or 'включи музыку' in task or 'сара включи музыку' in task or 'хочу музыку' in task or 'сара хочу музыку' in task or 'включи песню' in task:
        while not is_pressed('ctrl + u'):
            my_music()


    elif 'сара включи ютюб' in task or 'ютюб' in task or 'ютуб' in task or 'youtube' in task:
        text_before_music_in_youtube = 'что мне поискать в ютюбе?'
        start.say(text_before_music_in_youtube)
        start.runAndWait()
        # скажу, что именно нужно искать
        find_in_youtube = listen()

        text_read_what_find = find_in_youtube
        start.say('буду искать ' + text_read_what_find)
        start.runAndWait()
        # открывается ютюб
        browser = webdriver.Firefox()
        browser.implicitly_wait(5)
        browser.get('https://www.youtube.com/')
        # ставится мой запрос в поиск
        task_input = browser.find_element_by_css_selector("input[name='search_query']")
        task_input.send_keys(find_in_youtube)
        sleep(5)
        # click of button for find video
        button_find_video = browser.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
        button_find_video.click()
        sleep(4)
        #click to finded video
        click_under_video = browser.find_element(By.CSS_SELECTOR, "ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > ytd-thumbnail:nth-child(1) > a:nth-child(1)")
        click_under_video.click()





    elif 'гугл хром' in task or 'хром' in task or 'храм' in task:
        text = 'Открываю браузер Гугл Хром'
        start.say(text)
        start.runAndWait()
        subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        request(listen())
    #   elif 'закрой окно' in task or 'закрой это' in task or 'сара закрой окно' in task or 'помощница закрой окно':
      ##  text_before_close = 'закрываю'
     #   start.say(text_before_close)
     #   start.runAndWait()
      #  send("alt+f4")
    else:
        text_else = 'извините расул, я вас не поняла'
        start.say(text_else)
        start.runAndWait()


while True:
    request(listen())




