# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 19:59:22 2019

@author: User
"""

from nltk import pos_tag
from nltk import RegexpParser

text="learn php from guru99 and make study easy".split()
print("After Split:",text)
tokens_tag=pos_tag(text)
print("After Token",tokens_tag)