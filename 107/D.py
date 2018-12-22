#encoding utf 8
n = int(input())

a = list(int(i) for i in input().split())

# S = []
def set_s(a,x):
    S = []
    s = 0
    for i in range(n):
        if a[i] >= x:
            s += 1
        else:
            s -= 1
        S.append(s)
    return S

def count_inversion(a,x):
    S = set_s(a,x)
    count = sum(sum(m<n for m in a[i+1:]) for i,n in enumerate(a))
    return count

a_sort = a.sorted()
border = int(n/2)+1
while(1):
    count = count_inversion(a, a_sort[border])
    if count < int(n*(n+1)/4)+1:
        border =
    border = int(border/2)+1
































# 愚直に
# def midle_pos(midle):
#     return int(midle/2)
#
# m = a
# for i in range(1,n):
#     for j in range(n-i):
#         b = []
#         b += a[j:j+i]
#         b.sort()
#         m.append(b[midle_pos(i)])
#
# m.sort()
# # print(m)
# len = len(m)
# print(m[midle_pos(len)])
