def bubblesort(A):
    flag=True
    i=0
    count=0
    while flag:
        flag=False
        for j in range(len(A)-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]
                count+=1
                flag=True
        i+=1
    return A,count
    
N=int(input())
array=list(map(int,input().split()))
sorted_array,count=bubblesort(array)
print(*sorted_array)
print(count)
