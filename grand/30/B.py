#encoding:utf-8


L,N = map(int,input().split())

X = []
for i in range(N):
    tem = int(input())
    X.append(tem)

def decide_way(X,position):
    len = 0
    if position > X[0]:
        if L-position+X[0] >= position-X[-1]:
            len = L-position+X[0]
            new_pos = X[0]
            X.pop(0)
        else:
            len = position-X[-1]
            new_pos = X[-1]
            X.pop(-1)

    else:
        if X[0]-position >= position+(L-X[-1]):
            len = X[0]-position
            new_pos = X[0]
            X.pop(0)
        else:
            len = position+(L-X[-1])
            new_pos = X[-1]
            X.pop(-1)

    return X,new_pos,len

total_len = 0
new_pos = 0
for i in range(N):
    X,new_pos,len = decide_way(X,new_pos)
    total_len += len

print(total_len)
