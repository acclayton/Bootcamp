# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:39:01 2020

@author: Cory
"""

import enchant
d = enchant.Dict("en_US")



def spellcheck():
    word = input("Type a word ")
    while not d.check(word):
        word=input("Type a better word ")
        print("Congratulations you typed {} correctly".format(word))


def getWord():
    print("What is your name?")
    x=input()
    print("Hello {}".format(x))