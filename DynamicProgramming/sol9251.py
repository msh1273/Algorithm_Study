import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
a1 = list(a)
b1 = list(b)
result = []
for i in a1:
    for j in range(len(b1)):
        if i == b1[j] :
            result.append(i)
            b1 = b1[j+1:]
            break
print(result)