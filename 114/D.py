# encoding:utf-8

n = int(input())

import math

prime_dic = {}

for j in range(2,n):
    I=j
    s=0
    R=int(I)
    L=[]
    while s==0:
        for i in range(2,R+1):
            if I%i==0:
                I=I/i
                if I==1:
                    s=1
                if i in prime_dic.keys():
                    prime_dic[i] += 1
                else:
                    prime_dic[i] = 1
                break

large_num = 0
small_num = 0
for key in prime_dic.keys():
    if prime_dic[key] >= 4:
        large_num += 1
    if prime_dic[key] >= 2:
        small_num +=1
