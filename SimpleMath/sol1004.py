import sys

input = sys.stdin.readline

T = int(input().rstrip())
ans = []

for i in range(T):
    count = 0
    st_x, st_y, end_x, end_y = map(int, input().rstrip().split())
    n = int(input().rstrip())
    circle = []
    for _ in range(n):
        circle.append(list(map(int, input().rstrip().split())))
    
    for a, b, r in circle:
        is_start_in = ((st_x-a)**2 + (st_y-b)**2) < r**2
        is_end_in = ((end_x-a)**2 + (end_y-b)**2) < r**2
        if is_start_in ^ is_end_in:
            count += 1
            
    ans.append(count)

for i in ans:
    print(i)