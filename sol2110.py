import sys

input = sys.stdin.readline
# 집의 개수 N, 공유기의 개수 C
N, C = map(int, input().rstrip().split())

# 집의 좌표 Xi
Xi = []
for i in range(N):
    Xi.append(int(input().rstrip()))

Xi.sort()

# 최소 간격
start = 1
# 최대 간격
end = Xi[-1] - Xi[0]

answer = 0
while start <= end:
    mid = (start+end)//2
    count = 1   #처음에 공유기 하나 생성
    temp = Xi[0]    #길이를 비교하기 위한 기준
    for i in range(1, N):
        if Xi[i] >= temp + mid:
            count += 1
            temp = Xi[i]
    if count < C:   # 이 길이로는 공유기를 다 설치 못하는 경우 길이를 줄인다.
        end = mid - 1
    else:   #공유기 다 설치한 경우
        start = mid + 1
        answer = mid
print(answer)
