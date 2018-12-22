#encoding utf-8

a, b, c = map(int, input().split())

max = max(a, b, c)
min = min(a, b, c)

print(max-min)
