# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

def check(s):
    if len(s)%2==1:
        return False
    else:
        l = len(s)//2
        if s[:l]==s[l:]:
            return True
        else:
            return False


s = str(input())

for i in reversed(range(1,len(s))):
    # print(s[:i])
    if check(s[:i]):
        print(len(s[:i]))
        exit()
