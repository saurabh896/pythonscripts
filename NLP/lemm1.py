# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:21:54 2019

@author: User
"""

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
from collections import defaultdict
tag_map=defaultdict(lambda:wn.NOUN)
tag_map['J']=wn.ADJ
tag_map['V']=wn.VERB
tag_map['R']=wn.ADV

text = "guru99 is a totally new kind of learning  went on experience."
tokens=word_tokenize(text)
lemma_functions=WordNetLemmatizer()
for token,tag in pos_tag(tokens):
    lemma=lemma_functions.lemmatize(token,tag_map[tag[0]])
    print(token,"=>",lemma)