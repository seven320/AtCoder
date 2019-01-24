#encoding:utf-8


import random

import C

def make_problem():
    N = random.randint(1,100)
    Y = random.randint(1,2*10**4)*1000
    return N,Y

def check_clear(N,Y,answer):
    n = N
    y = Y
    true_answer = [-1,-1,-1]
    for i in range(n+1):
        for j in range(n-i+1):
            if i*9+j*4+n==y/1000:
                true_answer = [i,j,n-i-j]
    if true_answer == answer:
        return True
    else:
        print("true_answer:",true_answer)
        return False

for i in range(1000):
    N,Y = make_problem()
    answer = C.main(N,Y)

    if check_clear(N,Y,answer):
        print("clear")
    else:
        print("false_answer:",answer)
        print("false")
        print(N,Y)
