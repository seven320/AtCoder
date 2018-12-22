#encoding utf-8

a,b,c,d = map(int, input().split())

connect = 0
if abs(a-c) <= d:
    connect = 1
elif abs(a-b) <= d and abs(b-c) <= d:
    connect = 1
else:
    connect = 0

if connect == 1:
    print("Yes")
else:
    print("No")
