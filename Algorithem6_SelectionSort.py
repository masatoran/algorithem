def selectionsort(A,N):
    count=0
    for i in range(0,N-1):
        minj=i
        for j in range(i+1,N):
            if A[j] < A[minj]:
                minj=j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    return A,count

N=int(input())
array=list(map(int,input().split()))
sorted_array,count=selectionsort(array,N)
print(*sorted_array)
print(count)