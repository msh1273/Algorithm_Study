import sys

N, r, c = map(int, sys.stdin.readline().rstrip().split())

ans = 0

def solve(x, y, N):
    global ans
    if x == r and y == c:
        print(ans)
        exit(0)
    if N == 1:
        ans += 1
        return
    if not (x <= r < x+N and y <= c < y+N):
        ans += N*N
        return
    temp = N//2
    solve(x, y, temp)
    solve(x, y+temp, temp)
    solve(x+temp, y, temp)
    solve(x+temp, y+temp, temp)

solve(0,0, 2**N)
print(ans)