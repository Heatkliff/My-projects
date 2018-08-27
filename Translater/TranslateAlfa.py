# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 08:44:12 2018

@author: Heatcliph
"""

from googletrans import Translator

text_from = open('words.txt', 'r')
text_to = open('result.txt', 'w')
translator = Translator()

for line in text_from:
    result = translator.translate(line, dest='ru')
    text_to.write(result.text+'\n')
    print(line + "->" + result.text)

    

text_from.close()
text_to.close()