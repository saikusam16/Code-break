# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:48:29 2020

@author: edala
"""
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decryptor(key, message):
    return translateMessage(key, message)

def translateMessage(key, message):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex]) 
            num %= len(LETTERS)
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)