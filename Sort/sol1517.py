import sys
n = sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))

def mergeSort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    L = arr[:m]
    R = arr[m:]
    mergeSort(L)
    mergeSort(R)

    i=0
    j=0
    result = []
    while i <= len(L)-1 and j <= len(R)-1:
        if L[i] <= R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
            cnt += (len(L)-i)
    if i <= len(L)-1:
        result.append(L[i])
    if j <= len(R)-1:
        result.append(R[j])
    print(result)
if __name__ == '__main__':
    cnt = 0
    mergeSort(A)
    print(cnt)