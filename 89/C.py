#encoding:utf-8

import math
import itertools

n = int(input())
s = []
for i in range(n):
    s.append(str(input()))

chosen_names = {"m":0,"a":0,"r":0,"c":0,"h":0}

for name in s:
    if name[0] == "M":
        chosen_names["m"] += 1
    elif name[0] == "A":
        chosen_names["a"] += 1
    elif name[0] == "R":
        chosen_names["r"] += 1
    elif name[0] == "C":
        chosen_names["c"] += 1
    elif name[0] == "H":
        chosen_names["h"] += 1

answer = 0
capitals = list("march")
capital_set = itertools.combinations(capitals,3)
for capital in capital_set:
    answer += chosen_names[capital[0]] * chosen_names[capital[1]] * chosen_names[capital[2]]


print(answer)



# def combinations_count(n,r):
#     return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
