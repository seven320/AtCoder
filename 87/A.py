# encoding:utf-8

import numpy as np
import random

X = int(input())
A = int(input())
B = int(input())

cash = X
cash -= A

cash = cash - B*(cash // B)

print(cash)
