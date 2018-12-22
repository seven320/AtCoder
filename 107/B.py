#encoding utf-8

import numpy as np

H, W = map(int, input().split())

a = np.zeros((H,W))

for h in range(H):
    line = list(input())
    # print(line)
    for w in range(W):
        if line[w] == "#":
            line[w] = 1
        else:
            line[w] = 0
    a[h] = line


delete_line = 0
for h in range(H):
    h = h - delete_line
    if np.allclose(a[h,:], np.zeros(W)):
        a = np.delete(a, h, 0)
        delete_line += 1

delete_row = 0
for w in range(W):
    w = w - delete_row
    if np.allclose(a[:,w], np.zeros((1,H-delete_line))):
        a = np.delete(a, w, 1)
        delete_row +=  1

b = np.array(a, dtype = str)

for h in range(H-delete_line):
    for w in range(W-delete_row):
        if a[h,w] == 1:
            b[h,w] = "#"
        else:
            b[h,w] = "."

for i in range(H-delete_line):
    print("".join(b[i,:]))
