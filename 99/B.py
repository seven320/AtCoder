#encoding utf-8

a, b = map(int, input().split())

x = b-a
deep = (1+x)*x/2-b
print(int(deep))
