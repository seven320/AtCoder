# encoding:utf-8

import numpy as np
import random

a,b = map(str, input().split())

square_numbers = []
for i in range(1000):
    if i**2 <= 100100:
        square_numbers.append(i**2)
    else:
        break

if int(a+b) in square_numbers:
    print("Yes")
else:
    print("No")
