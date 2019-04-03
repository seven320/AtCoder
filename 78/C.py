# encoding:utf-8
import copy
import numpy as np
import random

N,M = map(int, input().split())

submit_time = (N-M)*100+M*1900

expe = 0
pro = (1/2)**M
for i in range(1,1000):
    expe += i*(1-pro)**(i-1)*pro

ans = expe*submit_time
print(round(ans))
