# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:08:40 2019

@author: User
"""

from nltk.stem import PorterStemmer
e_words=["wait","waiting","waited","waits","went"]
ps=PorterStemmer()
for w in e_words:
    rootWord=ps.stem(w)
    print(rootWord)