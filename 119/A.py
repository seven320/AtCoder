# encoding:utf-8
import copy
import numpy as np
import random

s = str(input())
yyyy,mm,dd = s.split("/")
ans = True
yyyy = int(yyyy)
mm = int(mm)
dd = int(dd)
if yyyy>=2020:
    ans = False
elif yyyy<=2018:
    pass
else:
    if mm>=5:
        ans = False
    elif mm<=3:
        pass
    else:
        pass

if ans:
    print("Heisei")
else:
    print("TBD")
