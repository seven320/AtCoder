# encoding:utf-8
import queue
from collections import deque
import time

que = queue.Queue()
dque = deque()

do_time = []
do_time.append(time.time()) # 計測

for i in range(10**6): # que
    que.put(i)

do_time.append(time.time())

while que.empty() == False:
    que.get()

do_time.append(time.time())

for i in range(10**6): # deque
    dque.append(i)

do_time.append(time.time())

while dque:
    dque.popleft()

do_time.append(time.time())


for i in range(len(do_time)-1):
    if i == 0 or i == 1:
        print("queue:",end = "")
    else:
        print("deque:",end = "")
    print(do_time[i+1] - do_time[i])
