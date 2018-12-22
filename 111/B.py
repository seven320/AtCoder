#encoding utf-8

n = int(input())

if n%111 == 0:
    print(n)
else:
    print(111*(int(n/111)+1))
