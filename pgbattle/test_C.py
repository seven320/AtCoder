# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

file_name = "./C.txt"

try:
    file = open(file_name, 'w')
    file.write("10000 10000\n")
    for i in range(10000):
        file.write(str(random.randint(1,10000))+" "+ str(random.randint(1,10000))+"\n")

except Exception as e:
    print(e)
finally:
    file.close()
