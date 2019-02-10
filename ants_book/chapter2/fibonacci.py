# encoding:utf-8

import copy
import numpy as np
import random
import time


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memory(n):
    if n <= 1:
        return n
    if memory[n] != 0:
        return memory[n]
    else:
        memory[n] = fib(n-1) + fib(n-2)
        return memory[n]

n=38

start_time = time.time()
print(fib(n))
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed_time:{0:0.4}".format(elapsed_time) + "[sec]")


start_time = time.time()
memory = [0]*(n+1)
print(fib_memory(n))
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed_time:{0:0.4}".format(elapsed_time) + "[sec]")
