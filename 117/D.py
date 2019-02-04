# encoding:utf-8

import copy
import numpy as np
import random

n,k = map(int,input().split())

a = [int(i) for i in input().split()]


# for i in range(len(a)):

sorted_a = sorted(a)
max_digit = 0


if k == 0:
    answer = 0
    for i in range(len(a)):
        answer += a[i]

else:
    while k >= 1:
        max_digit += 1
        k = k // 2

    # print(max_digit)
    def to_2_from_10(num):
        num_digit = [0]*40
        count = 0
        while num >= 1:

            if num % 2 == 1:
                num_digit[count] = 1
            else:
                pass
            num = num // 2
            count += 1
        # num_digit.reverse()
        return num_digit

    sum_digit = [0]*40
    for i in range(n):
        digit = to_2_from_10(a[i])
        # print(digit)
        for j in range(max_digit):
            if digit[j] == 0:
                sum_digit[j] += 1

    answer = 0
    for i in range(len(sum_digit)):
        if i >= max_digit:
            answer += 2**i*sum_digit[i]
        else:
            answer += 2**i*max(sum_digit[i],n-sum_digit[i])

print(answer)
