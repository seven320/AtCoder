#encoding utf 8

n, k = map(int, input().split())

pos = list(int(i) for i in input().split())

ans = abs(pos[0])+abs(pos[0]-pos[k-1])

for i in range(n-k+1):
    val = 0
    val += abs(pos[i] - pos[i+k-1])
    val += min(abs(pos[i]), abs(pos[i+k-1]))

    if val < ans:
        ans = val
print(ans)
