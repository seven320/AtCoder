#encoding:utf-8

N,M,X,Y=map(int, input().split())

x = list(int(i) for i in input().split())
y = list(int(i) for i in input().split())

x.sort()
y.sort()

war_flag = 0

if X >= Y:
    war_flag = 1

if x[-1] >= y[0]:
    war_flag = 1

if y[0] <= X:
    war_flag = 1

if x[-1] >= Y:
    war_flag = 1

#print
if war_flag == 1:
    print("War")
else:
    print("No War")
