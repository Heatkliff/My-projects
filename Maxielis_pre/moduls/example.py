# -*- coding: utf-8 -*-
from gtts import gTTS

import pygame
from pygame import mixer
mixer.init()

import os
import time
import datetime
import webbrowser
import subprocess

class Plugin:
    vk = None
    keys = []

    def __init__(self):
        print('Пример плагина')
        self.setkey(u'пример')

    def getkeys(self):
        ret = {}
        for key in self.keys:
            ret[key] = self
        return ret
    
    def setkey(self,key):
        self.keys.append(key)

    def call(self, msg):
        print("Сработал пример плагина")
        
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