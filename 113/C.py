#encoding:utf-8

n,m = map(int, input().split())
P = []
Y = []
for i in range(m):
    p,y = map(int,input().split())
    P.append(p)
    Y.append(y)

print(P,Y)
