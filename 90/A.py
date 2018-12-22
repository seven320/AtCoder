#encoding utf-8

import numpy as np

c = []
for i in range(3):
    c.append(list(str(input())))

answer = ""
for i in range(3):
    for j in range(3):
        if i == j:
            answer = answer + c[i][j]
print(answer)
