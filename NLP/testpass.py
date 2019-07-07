# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:21:12 2019

@author: User
"""

from random import choice
import string
import nltk.tokenize
length=8
def passgen(length):
    letters=[letter for letter in string.ascii_letters]
    digits=[digit for digit in string.digits]
    symbols=[symbol for symbol in string.punctuation]
    chars=letters+digits+symbols
    passwd=''.join(random.choice(chars) for x in range(length))
    print((passwd.tokenize_characters))
    return passwd
def main():
    length=int(input("number pls?"))
    if (length <=5):
        print("It is short.Please try again.")
    else:
        genpass=passgen(length)
        print(genpass)
        
if __name__ == '__main__':
    main()