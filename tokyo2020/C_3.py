a = [0,0,0,0]
B = [[0,3], [1,2], [0,4], [1,3]]


for b in B:
    left, right = b
    for i in range(left, right):
        a[i] += 1
print(a)

a = [0 for i in range(4)]
table = [0,0,0,0]
for b in B:
    left, right = b
    table[left] += 1
    if right >= len(table):
        continue
    table[right] -= 1

print(table)
tmp = 0
for i in range(len(a)):
    tmp += table[i]
    a[i] += tmp
print(a)

