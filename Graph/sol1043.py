import sys
# 사람수 n 파티수 m
n, m = map(int, sys.stdin.readline().rstrip().split())

# 진실을 아는 사람의 번호를 담은 리스트 tp_list
tp_list = set(sys.stdin.readline().rstrip().split()[1:])

# 파티 오는 사람 번호의 번호를 담은 리스트 pp_list
pp_list = []

# 거짓말 할 수 있는지 판단 1이면 거짓말 가능 0이면 불가능
can_list = []

for _ in range(m):
    pp_list.append(set(sys.stdin.readline().rstrip().split()[1:]))
    can_list.append(1)

for _ in range(m):
    for i, party in enumerate(pp_list):
        print(i, party)
        if tp_list.intersection(party):
            can_list[i] = 0
            tp_list = tp_list.union(party)

print(sum(can_list))
