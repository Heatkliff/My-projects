#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate


def main():
    to_translate = 'Bonjour comment allez vous?'
    print(translate(to_translate))
    print(translate(to_translate, 'ar'))
    print(translate(to_translate, 'ru'))
    text_from = open('words.txt', 'r')
    text_to = open('result.txt', 'w')
    for line in text_from:
        try:
            result = translate(line.encode("utf-8"), 'ru')
            text_to.write(result+'\n')
            print(line + "->" + result)
        except:
            resulted = '';
            for word in line.split(' '):
                try:
                    result = translate(word.encode("utf-8"), 'ru')
                    text_to.write(result+' ')
                    resulted+=result
                except:
                    continue
            text_to.write('\n')
            print(line + "->" + resulted)

if __name__ == '__main__':
    main()
