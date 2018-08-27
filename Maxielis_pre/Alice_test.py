# Библиотеки распознавания и синтеза речи
import speech_recognition as sr
from gtts import gTTS

# Воспроизведение речи
import pygame
from pygame import mixer
mixer.init()

import os
import sys
import time
import datetime
import logging
import webbrowser
import subprocess

class Speech_AI:

    def __init__(self):

        path = 'moduls/'
        plugins = {}
        self.cmds = {}
        sys.path.insert(0, path)
        for f in os.listdir(path):
            fname, ext = os.path.splitext(f)
            if ext == '.py':
                mod = __import__(fname)
                plugins[fname] = mod.Plugin()
        sys.path.pop(0)
        
        for plugin in plugins.values():
            for key, value in plugin.getkeys().items():
                self.cmds[key] = value
        
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

        
        now_time = datetime.datetime.now()
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        self._mp3_nameold='111'

    def work(self):
        print("Минутку тишины, пожалуйста...")
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)
        #print(list(self.cmds.keys()))
        try:
            while True:
                print("Скажи что - нибудь!")
                with self._microphone as source:
                    audio = self._recognizer.listen(source)
                print("Поняла, идет распознавание...")
                try:
                    statement = self._recognizer.recognize_google(audio, language="ru_RU")
                    statement=statement.lower()
                    prefixes = ['алиса', 'лиса']
        
                    for prefix in prefixes:
                        if((statement.find(prefix)!=-1)):
                            for key in list(self.cmds.keys()):
                                if((statement.find(key)!=-1)):
                                    print(key)
                                    self.cmds[key].call(key)
                                    break
                    
                    print("Вы сказали: {}".format(statement))
                    
                    if((statement.find("закройся")!=-1)):
                        answer = "Пока!"
                        self.say(str(answer))
                        while pygame.mixer.music.get_busy():
                            time.sleep(0.1)
                        sys.exit()
                    
                    
                   
                    
                except sr.UnknownValueError:
                    print("Упс! Кажется, я тебя не поняла, повтори еще раз")
                except sr.RequestError as e:
                    print("Не могу получить данные от сервиса Google Speech Recognition; {0}".format(e))
        except KeyboardInterrupt:
            self._clean_up()
            print("Пока!")
        
    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def openurl(self, url, ans):
        webbrowser.open(url)
        self.say(str(ans))
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    def say(self, phrase):
        tts = gTTS(text=phrase, lang="ru")
        tts.save(self._mp3_name)

        # Play answer
        mixer.music.load(self._mp3_name)
        mixer.music.play()
        if(os.path.exists(self._mp3_nameold)):
            os.remove(self._mp3_nameold)
       
        now_time = datetime.datetime.now()
        self._mp3_nameold=self._mp3_name
        self._mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"
        
        
    def command(message, self):
        #words = message.split()
    
        prefixes = ['алиса']
        
        for prefix in prefixes:
            if((message.find(prefix)!=-1)):
                for key in self.cmds:
                    if((message.find(prefix)!=-1)):
                        self.cmds[key].call(message)
                
    
        #if words[0].lower() in prefixes:
            #if len(words) > 1 and words[1] in self.cmds:
                #self.cmds[words[1].lower()].call(message)

    def _clean_up(self):
        def clean_up():
            os.remove(self._mp3_name)


def main():
    ai = Speech_AI()
    ai.work()

main()
