#encoding:utf-8

n = int(input())
s = [str(i) for i in input().split()]
s_ = set(s)
if "Y" in s:
    answer = "Four"
else:
    answer = "Three"

print(answer)
