# -*- coding: utf-8 -*-


class Plugin:
    vk = None
    keys = []

    def __init__(self):
        print('Проги')
        self.setkey(u'word')
        self.setkey(u'ворд')

    def getkeys(self):
        ret = {}
        for key in self.keys:
            ret[key] = self
        return ret
    
    def setkey(self,key):
        self.keys.append(key)

    def call(self, msg):
        #self.openurl('"C:\Games\Skyrim Legendary Edition\GameLauncher.exe"', "Приятной игры")
        print("Тут откроется ворд")