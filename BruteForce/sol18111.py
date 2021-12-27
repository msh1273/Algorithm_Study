import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
ground = []
for i in range(n):
    ground += list(map(int,input().split()))
top, bottom = max(ground), min(ground)
ground = sorted(ground)[::-1]
# 블럭을 깎아서 모은 다음 쌓아야 계산이 편하다.

minCount = float('inf')
maxTop = 0

for i in range(bottom, top+1):
    count = 0
    b2 = int(b)
    for j in ground:
        if j > i:
            count += (j-i)*2
            b2 += j-i
        elif j < i:
            count += i-j
            b2 -= i-j
            # 블럭이 모자란 경우
            if b2 < 0:
                break
        # 최소 노력보다 이미 큰 경우
        if count > minCount:
            break
    else:
        if count <= minCount:
            minCount = count
            if i >= maxTop:
                maxTop = i
print(minCount,maxTop)