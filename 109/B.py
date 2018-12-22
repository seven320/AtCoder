#encoding utf-8

n = int(input())
words = [0]*n
for i in range(n):
    words[i] = str(input())

state = 1

for i in range(n-1):
    # print(list(words[i])[-1],list(words[i+1])[0])
    if list(words[i])[-1] == list(words[i+1])[0]:
        state = 1
    else:
        state = 0
        break

if len(list(set(words))) < n:
    state = 0

if state == 1:
    print("Yes")
else:
    print("No")
