#辞書
#しかしリソースの超過をしてしまうのでリストではなく集合を使う
dictionary=[]
for _ in range(int(input())):
    ope,element=input().split()
    if ope == 'insert':
        dictionary.append(element)
    else:
        if element in dictionary:
            print('yes')
        else:
            print('no')
            
dictionary = set() 

for _ in range(int(input())):
    ope, element = input().split()
    
    if ope == 'insert':
        dictionary.add(element) 
    else:
        print('yes' if element in dictionary else 'no') 