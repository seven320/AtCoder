#encoding:utf-8

import numpy as np
N,Q = map(int,input().split())

A = [int(i) for i in input().split()]
X = []
for i in range(Q):
    X.append(int(input()))

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

def turn_taka(answer,game_A):
    answer += game_A[-1]
    game_A.pop(-1)
    return answer,game_A

def turn_ao(game_A):
    tem = getNearestValue(game_A,x)
    game_A.remove(tem)
    return game_A

def game(x):
    answer = 0
    game_A = sorted(A)
    while True:
        if len(game_A) > 0:
            answer,game_A = turn_taka(answer,game_A)
        else:
            break
        if len(game_A) > 0:
            game_A = turn_ao(game_A)
        else:
            break
    return answer

#chose x
for x in X:

    print(game(x))
