import sys
import math
#초항a 공차d
a, d = map(int, sys.stdin.readline().rstrip().split())
#쿼리수 q
q = int(sys.stdin.readline().rstrip())

for i in range(q):
    answer = []
    n, l, r = map(int, sys.stdin.readline().rstrip().split())
    if n == 1:
        if l == 1:
            ans = (r*(2*a + (r-1)*d))/2
        else:
            ans = (r*(2*a + (r-1)*d))/2 -((l-1)*(2*a + ((l-1)-1)*d))/2

        print(int(ans))
    if n == 2:
        if l == r:
            m = a + (l-1)*d
            print(m)
        else:
            m1 = a + (l-1)*d
            m2 = a + (l)*d
            gc = math.gcd(m1, m2)
            if r - l == 1:
                print(gc)
            else:
                for k in range(l+2, r+1):
                    m2 = a + (k-1)*d
                    gc = math.gcd(m2, gc)
                print(gc)
