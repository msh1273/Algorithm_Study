import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

tree = list(map(int, sys.stdin.readline().rstrip().split()))

start = 1
end = max(tree)

mid = 0
while start <= end:
    mid = (start+end)//2
    ans=0
    for i in tree:
        if i > mid:
            ans += (i-mid)
    if ans >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)