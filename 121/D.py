# encoding:utf-8
import copy
import numpy as np
import random

a,b = map(int,input().split())
# 1digit
def function(n):
    if n==0 or n==1:
        return n
    else:
        if n%4==0:
            return n
        elif n%4==1:
            return 1
        elif n%4==2:
            return n+1
        else:
            return 0

if a==0:
    print(function(b))
    exit()

else:
    print(function(a-1)^function(b))





'''
# F(0,n)を求める
def F(n):
    if n==0:
        tmp_ans = 0
    else:
        true_count = (n+1)//2
        if (n+1)%2==0:
            if true_count%2==0:
                tmp_ans = 0
            else:
                tmp_ans = 1
        else:
            if true_count%2==0:
                tmp_ans = n
            else:
                if n%2==0:
                    tmp_ans = n+1
                else:
                    tmp_ans = n-1

    return tmp_ans

max_digit = 0
num = b
while num > 0:
    max_digit += 1
    num = num//2

a_digits= []
b_digits = []
digits = []

A = F(a-1)
B = F(b)
# print(A,B)
for i in range(max_digit):
    a_digits.append(A%2)
    b_digits.append(B%2)
    A = A//2
    B = B//2

for i in range(max_digit):
    if (a_digits[i] == 1 and b_digits[i] == 1) or (a_digits[i] == 0 and b_digits[i]==0):
        digits.append(0)
    else:
        digits.append(1)

ans = 0
for i in range(max_digit):
    ans += digits[i]*2**i

print(ans)
'''
'''
if a == b:
    print(a)
    exit()

def xor_0(a,b):
    if((b-a+1)//2)%2 == 0:
        if (b-a+1)%2==0:
            digit = 0
        else:
            if a%2==0:
                # 0 xor 0
                digit = 1
            else:
                # 1 xor 1
                digit = 1
    else:
        if (b-a+1)%2==0:
            digit = 1
        else:
            if a%2==0:
                # 0 xor 0
                digit = 1
            else:
                # 0 xor 1
                digit = 0

    return digit

max_digit = 0
num = b
while num > 0:
    max_digit += 1
    num = num//2

def digit_xor(a,b,i):
    if i == 0:
        return xor_0(a,b)
    else:
        count = 0
        posi_a = a%(2**(i+1))
        if posi_a>2**i:
            count += 2**i-a+1
        elif posi_a==0:
            pass
        else:
            count += 2**i

        posi_b = b%(2**(i+1))
        if posi_b > 2**i:
            count += 2**i
        else:
            count += posi_b

    if count%2==0:
        return 0
    else:
        return 1


digits = []
for i in range(max_digit):
    digits.append(digit_xor(a,b,i))

ans = 0
print(digits)
for i in range(len(digits)):
    ans += digits[i]*2**i

print(ans)
'''
