x,y=map(int,input().split())
while(True):
    if x % y == 0:
        break
    temp = x
    x = y
    y = temp % y
print(y)
