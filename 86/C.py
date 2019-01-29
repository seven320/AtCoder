# encoding:utf-8

import numpy as np
import random

n = int(input())
x = []
t = []
y = []
for i in range(n):
    t_tem,x_tem,y_tem = map(int,input().split())
    t.append(t_tem)
    x.append(x_tem)
    y.append(y_tem)

def check_move(t,x,y):
    check = True
    #距離が長いとダメ
    if x+y > t:
        check = False
    #偶奇の組み合わせだとダメ
    elif x+y+t%2 == 1:
        check = False

    return check

answer = True
x_now = 0
y_now = 0
t_now = 0
for i in range(n):
    answer *= check_move(t[i]-t_now,x[i]-x_now,y[i]-y_now)
    t_now = t[i]
    x_now = x[i]
    y_now = y[i]

if answer:
    print("Yes")
else:
    print("No")
