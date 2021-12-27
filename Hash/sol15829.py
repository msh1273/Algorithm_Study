import sys
a = list("abcdefghijklmnopqrstuvwxyz")
alphabet = {a[i] : i+1 for i in range(len(a))}

l = int(sys.stdin.readline().rstrip())

r = 31
M = 1234567891

aList = list(sys.stdin.readline().rstrip())

s = 0
for i in range(l):
    score = alphabet[aList[i]]
    s += (score * (r**i))

print(s % M)