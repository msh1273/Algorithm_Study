import sys

input = sys.stdin.readline

remoteController = set(str(i) for i in range(10))

#현재 위치
now = 100
#이동할 위치
N = int(input().rstrip())

#고장난 버튼 수
M = int(input().rstrip())

#고장난 버튼이 있다면
if M != 0:
    MList = set(list(map(str, input().rstrip().split())))
    #살아있는 버튼
    remoteController = remoteController - MList

tempCount = abs(now - N)

for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if i[j] not in remoteController:
            break
        elif j == len(i)-1:
            tempCount = min(tempCount, abs(int(i)-N) + len(i))
print(tempCount)