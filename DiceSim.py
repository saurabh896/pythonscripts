# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:19:29 2019

@author: Saurabh Kadam
"""

import random as rn

print("Welcome to simulation for Dice game")

print("Guess a number that comes on Dice")
GuessNum=input()
Guess=False
print()
counter=0
print("Odds are ",1/36)
#probability of number##
while(Guess==False):
    num=rn.randint(1,6)
    counter=counter+1
    print(num)
    if GuessNum==num:
        print('Odds with you')
        Guess=True
        break
print('It takes',counter,'turns for your restulet')
    
