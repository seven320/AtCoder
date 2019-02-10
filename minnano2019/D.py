# encoding:utf-8

import copy
import numpy as np
import random
import itertools

l = int(input())

a = []
for i in range(l):
    a.append(int(input()))

source = list(range(l+1))

combinations = list(itertools.combinations(source,2))

answer = 10**10
# print(combinations)
for combination in combinations:
    a_tem = copy.deepcopy(a)
    goal = combination[1]
    start = combination[0]
    position = start
    # print(start,goal)
    # while True:
    #     a_tem[position] -= 1
    #     position -= 1
    #     if position == start:
    #         break
    #
    # position = goal
    while True:
        if a_tem[position] >= 2:
            if a_tem[position] % 2 == 1:
                a_tem[position] = 1
            else:
                a_tem[position] = 0
        else:
            if a_tem[position] == 0:
                a_tem[position] = 2

        position += 1
        if position == goal:
            break

    com_source = list(range(goal-start))
    combinations2 = itertools.combinations(com_source,2)
    # print(a_tem)
    if sum(a_tem)-l >= answer:
        pass
    else:
        for combination2 in combinations2:
            count = 0
            a_np = np.array(a_tem)
            # print(a_np)
            start_2 = combination2[0]
            goal_2 = combination2[1]
            start_2 += start
            goal_2 += start
            a_np[start_2:goal_2] -= 1
            # print(a_np)
            for i in range(l):
                if a_np[i] == -1:
                    count += 1
                else:
                    count += a_np[i]
                if count >= answer:
                    break
            answer = min(answer,count)

print(answer)
