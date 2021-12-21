import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().rstrip().split()))
m = int(input())
mList = list(map(int, input().rstrip().split()))

a = Counter(nList)
for key in mList:
    if key in a.keys():
        print(a[key], end=' ')
    else:
        print(0, end=' ')