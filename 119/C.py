# encoding:utf-8
import copy
import numpy as np
import random



def to_4digit(i,n):
    digits = [0 for i in range(n)]
    digit = 0
    while(i>=1):
        digits[digit] = i%4
        digit += 1
        i//=4
    return digits

def main():
    n,a,b,c = map(int,input().split())
    l = []
    for i in range(n):
        l.append(int(input()))
    print(solve(n,a,b,c,l))

def solve(n,a,b,c,l):
    ans = 10**20
    for i in range(4**n-1):
        choice = to_4digit(i,n)
        abc = [0 for i in range(3)]
        mp = 0
        # print(choice)
        for j in range(len(choice)):
            if choice[j]==3:#trash
                pass
            else:
                if abc[choice[j]]!=0:
                    mp += 10
                abc[choice[j]] += l[j]
        if 0 in abc:
            pass
        else:
            mp += abs(abc[0]-a)+abs(abc[1]-b)+abs(abc[2]-c)
            if ans>mp:
                ans = mp


        # print(ans)
    return ans


if __name__ == "__main__":
    main()
