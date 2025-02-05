def binarySearch(inputArray:list,value):
    left=0
    right=len(inputArray)
    while left < right:
        mid = (left+right)//2
        if value == inputArray[mid]:
            return True
        elif value < inputArray[mid]:
            right = mid
        elif value > inputArray[mid]:
            left = mid + 1
        else:
            return False
        
        
n=int(input())
S=sorted(list(set(map(int,input().split()))))
q=int(input())
T=list(set(map(int,input().split())))

count=0
for i in T:
    if binarySearch(S,i):
        count+=1
print(count)
