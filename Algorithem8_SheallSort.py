def bubblesort(array):
    array = array.copy()
    i=0
    flag=True
    while flag:
        flag=False
        for j in range(len(array)-1,i,-1):
            if int(array[j][1]) < int(array[j-1][1]):
                array[j],array[j-1]=array[j-1],array[j]
                flag=True
    i+=1
    return array

def selectionsort(array):
    array = array.copy()
    for i in range(len(array)-1):
        minj=i
        for j in range(i+1,len(array)):
            if int(array[j][1]) < int(array[minj][1]):
                minj=j
        array[i], array[minj] = array[minj], array[i]
    return array

N=int(input())
li=list(map(str,input().split()))
bubble=bubblesort(li)
select=selectionsort(li)

print(*bubble)
print('Stable')
print(*select)
print('Not stable' if bubble != select else 'Stable')
