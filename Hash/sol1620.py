import sys

input = sys.stdin.readline

#도감에 입력된 포켓몬 개수 N, 맞춰야하는 문제의 수 M
N, M = map(int, input().rstrip().split())

pList = []
for i in range(N):
    pList.append(input().rstrip())

rev_pDict = dict(enumerate(pList, start=1))
pDict = dict(map(reversed, enumerate(pList, start=1)))

for i in range(M):
    poketmon = input().rstrip()
    if poketmon.isalpha():
        value = pDict[poketmon]
        print(value)
    else:
        value = rev_pDict[int(poketmon)]
        print(value)