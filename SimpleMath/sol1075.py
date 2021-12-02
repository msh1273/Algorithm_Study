n = input()
f = int(input())

n = n[:-2]

for i in range(100):
    tempN = n
    ans = ''
    if i < 10:
        ans = '0' + str(i)
        tempN = tempN + ans
    else:
        ans = str(i)
        tempN += ans
    if int(tempN) % f == 0:
        if i<10:
            print('0'+str(i))
        else:
            print(str(i))
        break