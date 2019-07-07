# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:19:42 2019

@author: User
"""

import argparse
import sys

try:
    parser=argparse.ArgumentParser()
    parser.add_argument("square",help="display number",type=int)
    args=parser.parse_args()
    print(sys.argv)
    print(sys.argv[1])
except:
    e=sys.exc_info()[0]
    print(e)