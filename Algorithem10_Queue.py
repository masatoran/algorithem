n,q=map(int,input().split())
keys=[]
values=[]
for _ in range(n):
    key,value=input().split()
    keys.append(key)
    values.append(int(value))

sumOfValue=0
while len(keys) != 0:
    key=keys[0]
    value=values[0]
    if value <= q:
        sumOfValue+=value
        print('{} {}'.format(key,sumOfValue))
        del keys[0]
        del values[0]
    elif value > q:
        sumOfValue+=q
        new_value=value-q
        keys.append(keys[0])
        values.append(new_value)
        del keys[0]
        del values[0]
