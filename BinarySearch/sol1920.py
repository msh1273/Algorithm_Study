import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return True
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input().rstrip())
n_list = sorted(list(map(int, input().rstrip().split())))

m = int(input().rstrip())
m_list = list(map(int, input().rstrip().split()))

for i in m_list:
    if binary_search(n_list, i, 0, n-1):
        print(1)
    else:
        print(0)