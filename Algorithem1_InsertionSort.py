#挿入ソート
#InsertionSort
def insertionSort(A,N):
    for i in range(N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)
        
A=int(input())
array=list(map(int,input().split()))
insertionSort(array,A)
