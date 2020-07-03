# encoding:utf-8
import copy
import numpy as np
import random
import pandas as pd
import torch


def find_primes(n):
    candidates = [int(i) for i in range(2,n+1)]
    if len(candidates)<=0:
        # print("error")
        return None
    candidates.reverse()
    now = candidates.pop()
    primes = []
    primes.append(now)
    while len(candidates)>0:
        for candidate in candidates:
            if candidate % now == 0:
                candidates.remove(candidate)
        now = candidates.pop()
        primes.append(now)
    # primes = primes + candidates
    return primes

print(find_primes(10 ** 4))
