#encoding utf-8

n = int(input())

max_donut = int(n/7)+1
judge = False
for i in range(max_donut):
    if (n-i*7)%4 == 0:
        judge = True

if judge == 1:
    print("Yes")
else:
    print("No")
