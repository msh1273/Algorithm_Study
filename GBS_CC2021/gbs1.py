import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
stX, stY = map(int, sys.stdin.readline().rstrip().split())
endX, endY = map(int, sys.stdin.readline().rstrip().split())

if N == 1 or M == 1:
    if stX == endX and stY == endY:
        print("YES")
    else:
        print("NO")
else:
    #시작 위치가 홀홀, 짝짝인 경우
    if (stX % 2 == 1 and stY % 2 == 1) or (stX % 2 == 0 and stY % 2 == 0):
        if endX % 2 == 0 and endY % 2 == 0:
            print("YES")
        elif endX % 2 == 1 and endY % 2 == 1:
            print("YES")
        else:
            print("NO")
    #시작위치가 홀짝, 짝홀인 경우
    if (stX % 2 == 0 and stY % 2 == 1) or (stX % 2 == 1 and stY % 2 == 0):
        if endX % 2 == 1 and endY % 2 == 0:
            print("YES")
        elif endX % 2 == 0 and endY % 2 == 1:
            print("YES")
        else:
            print("NO")