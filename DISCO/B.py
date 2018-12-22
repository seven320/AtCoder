#encoding utf-8
import numpy as np

n = int(input())

def classify(x,y):
    judge = 0
    if (-x+0.5 <= y <= -x+1.5) and (x-0.5 <= y <= x+0.5):
        judge = 1
    return judge

table = np.zeros((n+1,n+1))
for i in range(n+1):
    for j in range(n+1):
        x = float(i/n)
        y = float(j/n)
        table[i,j] = classify(x,y)

# print(table)
count_black = 0
for x in range(n):
    for y in range(n):
        if 4 == table[x:x+2,y:y+2].sum():
            count_black += 1

if n % 10 == 0:
    count_black += n//10*2-1
print(int(count_black))
