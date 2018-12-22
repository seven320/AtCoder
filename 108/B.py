## -*- coding: utf-8 -*-

x_1, y_1, x_2, y_2 = map(int, input().split())

a = [x_2-x_1,y_2-y_1]

x_3 ,y_3 = x_2-a[1], y_2+a[0]

x_4, y_4 = x_3-a[0], y_3-a[1]

print(x_3, y_3, x_4, y_4)
