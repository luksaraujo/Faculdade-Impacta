from math import *
x = input().split()
y = input().split()
x1, y1, x2, y2 = float(x[0]), float(x[1]), float(y[0]), float(y[1])
cal = sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
print('%.4f' %cal)
