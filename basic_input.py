
# coding: utf-8

# atcoderで使用する基本的な標準入力まとめ

# まずは数字の入力でよく使うもの
#
# スーペースで切ってそれぞれの変数に入力
#
# 入力例)
# 1 6 3

a, b, c = map(int, input().split())
print(a,b,c)

# 最初、与えられる数列の個数が与えられて、その数だけリストに格納
#
# 入力例)
# 6
# 3 6 4 8 9 1

list = []
n = input()
# num = list(int(i) for i in input().split())

num1 = [int(i) for i in input().split()]

print(num1,"\n")


# 単語をstrで入力してから１文字づつリストに格納
#
# 入力例)
# kyoto
# tokyo

# In[9]:

s = list(input())
t = list(input())


# 行列のサイズm*nが最初に与えられ、その行列をリストに格納
#
# 入力例)
# 2 3
# 1 2 3
# 2 3 4

# In[9]:

m, n = map(int, input().split())
A = []
for i in range(m):
    A.append([int(i) for i in input().split()])

print(A)
