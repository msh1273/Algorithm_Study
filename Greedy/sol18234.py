import sys

# N: 당근 종류 T: 재배 일
# wi: 처음 당근의 맛  pi: 당근의 맛을 증가시켜줄 영양제(pi를 한번 주면 당근의 맛은 wi+pi가 됨.) , pi는 N(당근 종류)만큼 T개 씩 있다.
# pi >= wi, T >= N
# i에 당근이 없으면 심고 아니면 영양제를 준다.

N, T = map(int, sys.stdin.readline().split())

carrot = []
for _ in range(N):
    wi, pi = map(int, sys.stdin.readline().split())
    carrot.append([wi, pi])


carrot = sorted(carrot, key=lambda x: [-x[1], -x[0]])
print(carrot)

taste = 0

days = T-1

for w, p in carrot:
    taste += (p*days) + w
    days -= 1

print(taste)
