# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())

N,K = LI()
D = [str(i) for i in input().split()]


def main():
    ans = N
    while True:
        for i in range(K):
            # print(list(str(ans)))
            if D[i] in list(str(ans)):
                # print(ans)
                ans += 1
                # ans += 10**max((len(str(ans))-list(str(ans)).index(D[i])-1),0)
                break
            if i == K - 1:
                return ans

print(main())
