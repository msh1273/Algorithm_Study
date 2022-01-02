import sys

X = list(map(int, sys.stdin.readline().rstrip()))

flag = True

if len(X) == 2:
    print("NON ALPSOO")
    flag = False
else:
    sl = X[1] - X[0]
    el = X[-1] - X[-2]
    if sl > 0 and el < 0:
        for i in range(2, len(X)):
            tsl = X[i] - X[i-1]
            # 오르막
            if tsl > 0:
                #경사가 이전과 같다면
                if tsl == X[i-1] - X[i-2]:
                    continue
                #경사가 이전과 다름
                else:
                    #이전 경사가 내리막이었다면 오르막은 아무높이 상관 없음
                    if X[i-1] - X[i-2] < 0:
                        continue
                    else:
                        print("NON ALPSOO")
                        flag =False
                        break
            #내리막
            elif tsl < 0:
                if tsl == X[i-1] - X[i-2]:
                    continue
                #경사가 이전과 다름
                else:
                    #이전 경사가 오르막이었다면 오르막은 아무높이 상관 없음
                    if X[i-1] - X[i-2] > 0:
                        continue
                    else:
                        print("NON ALPSOO")
                        flag = False
                        break
    else:
        print("NON ALPSOO")
        flag = False

if flag:
    print("ALPSOO")
