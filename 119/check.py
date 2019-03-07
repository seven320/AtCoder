# encoding:utf-8
import copy
import numpy as np
import random

import C
import C_answer







for i in range(100):
    n = random.randint(3,5)
    abc = [0 for _ in range(3)]
    for j in range(3):
        abc[j] = random.randint(1,100)
    abc.sort()
    c = abc[0]
    b = abc[1]
    a = abc[2]
    l = []
    for j in range(n):
        l.append(random.randint(1,1000))

    my_ans = C.solve(n,a,b,c,l)

    other_ans = C_answer.solve(n,a,b,c,l)
    if my_ans != other_ans:
        print(n,a,b,c)
        print(l)
        print("{0}:{1}".format(my_ans,other_ans))
