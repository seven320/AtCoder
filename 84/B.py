# encoding:utf-8

import copy
import numpy as np
import random

a,b = map(int, input().split())
s = str(input())

s = s.split("-")
if len(s[0]) == a and len(s[1]) == b:
    try:
        int(s[0]) and int(s[1])
        print("Yes")
    except:
        print("No")
        
else:
    print("No")
