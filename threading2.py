# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:36:54 2019

@author: User
"""

import threading,time

print('start of program')

def takeNap():
    time.sleep(5)
    print('Wake up!')
threadObj=threading.Thread(target=takeNap)
threadObj.start()
print('End of program')