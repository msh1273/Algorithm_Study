
# 2원과 5원으로만 거스름돈
# 동전의 갯수가 최소가 되도록 주자

n = int(input())

count5 = 0
count2 = 0

answer = 0

count5 = n//5
if count5 == 0:
    if n % 2 == 0:
        count2 = n//2
        answer = count2
    else:
        answer = -1
else:
    # 5원의 개수를 하나씩 줄이면서 맞는지 확인해본다.
    for i in range(count5, -1, -1):
        if i*5 == n:
            answer = i
            break
        else:
            temp = n
            temp -= i*5
            if temp % 2 == 0:
                answer = i + (temp//2)
                break

print(answer)
