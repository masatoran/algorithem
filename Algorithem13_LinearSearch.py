n=int(input())
S=list(set(map(int,input().split())))
q=int(input())
T=list(set(map(int,input().split())))

count=0
for i in S:
    for j in T:
        if j == i:
            count+=1
            break
print(count)
