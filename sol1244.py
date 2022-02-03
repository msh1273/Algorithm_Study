import sys

N = int(sys.stdin.readline().rstrip())

swi = list(map(int, sys.stdin.readline().rstrip().split()))

stu = int(sys.stdin.readline().rstrip())

for i in range(stu):
    s, num = map(int, sys.stdin.readline().rstrip().split())
    # 남자면 받은 수 의 짝수번 스위치는 상태를 바꿔라
    if s == 1:
        for i in range(N):
            if (i+1) % num == 0:
                swi[i] = swi[i] ^ 1
    # 여자인 경우 받은걸 중심으로 좌우 대칭으로 대칭이 아닐때 까지 찾기
    elif s == 2:
        c = 1
        if num == 1:
            swi[0] = swi[0] ^ 1
        else:
            start = 0
            end = 0
            while True:
                if num-1-c >= 0 and num-1+c < N:
                    if swi[num-1-c] == swi[num-1+c]:
                        c += 1
                    else:
                        start = num-1-c
                        end = num-1+c
                        break
                else:
                    start = num-1-c
                    end = num-1+c
                    break
            for i in range(start+1, end):
                swi[i] = swi[i] ^ 1

count = 0
for i in range(len(swi)):
    print(swi[i], end=' ')
    count += 1
    if count == 20:
        print()
        count = 0
