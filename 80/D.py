N,C = map(int,input().split())
tv_times = [[int(j) for j in input().split()] for i in range(N)]

channells = {}
for i in range(C+1):
    channells[i] = []
max_end = -1

for i in range(N):
    s,g,c = tv_times[i]
    max_end = max(max_end,g)
    channells[c] += [s,g]

tv_times = []
f = [0 for i in range(max_end+1)]
for cha in channells.keys():
    remove_list = []
    time = channells[cha]
    time.sort()
    for i in range(1,len(time)-1):
        if time[i] == time[i+1]:
            remove_list.append(time[i])
    time = list(set(time)-set(remove_list))
    time.sort()
    for i in range(len(time)//2):
        f[max(time[2*i]-1,0)] += 1
        f[time[2*i+1]] -= 1
ans = -1
for i in range(1,max_end+1):
    f[i] += f[i-1]
    if ans < f[i]:
        ans = f[i]

print(ans)
