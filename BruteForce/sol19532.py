import sys

input = sys.stdin.readline().rstrip().split()
# ax + by = c
# dx + ey = f

#a, b, c, d, e, f = map(int, input)

# for x in range(-999, 1000):
#     for y in range(-999, 1000):
#         if a*x + b*y == c and d*x + e*y == f:
#             print(x, y)

a, b, x, c, d, y = map(int, input)
# n = ad-bc
n = a*d-b*c

xx = (d*x - b*y)//n
yy = (-c*x + a*y)//n

print(xx, yy)
