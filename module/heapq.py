import heapq
"""
優先度付きキュー
大小関係を保ちつつ，キューを使える．
最小値をO(logN)で取り出す
要素をO(logN)で挿入できる

通常O(N)
"""
a = []

for i in reversed(range(10)):
    heapq.heappush(a, i) # 挿入，

for i in range(len(a)):
    print(heapq.heappop(a)) # 最小の値から取り出す
