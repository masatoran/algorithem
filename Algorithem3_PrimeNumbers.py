import math

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        a=int(math.sqrt(n))
        for i in range(3,a+1,2):
            if n % i == 0:
                return False
                break
        return True
        
N=int(input())
count=0
for i in range(N):
    if is_prime(int(input())):
        count+=1
print(count)
