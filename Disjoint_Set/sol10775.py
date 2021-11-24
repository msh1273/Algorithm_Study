import sys

g = int(sys.stdin.readline().rstrip())

p = int(sys.stdin.readline().rstrip())

count = 0

plane_list = []
for i in range(p):
    plane_list.append(int(sys.stdin.readline().rstrip()))

gate_parent = [i for i in range(g+1)]


def find(i):
    if gate_parent[i] == i:
        return i
    gate_parent[i] = find(gate_parent[i])
    return gate_parent[i]


for i in plane_list:
    temp = find(i)
    if temp == 0:
        break
    gate_parent[temp] = gate_parent[temp-1]
    count += 1

print(count)
