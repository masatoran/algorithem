n = int(input())
minv = float('inf')
maxv = float('-inf')

for _ in range(n):
    price = int(input())
    maxv = max(maxv, price - minv)
    minv = min(minv, price)

print(maxv)