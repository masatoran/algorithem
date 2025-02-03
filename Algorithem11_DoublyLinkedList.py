from collections import deque

li = deque()

def addValueToListFirst(array: deque, value) -> None:
    array.appendleft(value)  # 先頭に追加

n = int(input())
for _ in range(n):
    e = input().split()
    command = e[0]
    
    if command == 'insert':
        addValueToListFirst(li, e[1])
    elif command == 'delete':
        try:
            li.remove(e[1])  # 最初に見つかった e[1] を削除
        except ValueError:
            pass  # 値が存在しない場合は無視
    elif command == 'deleteFirst':
        li.popleft()  # 先頭を削除
    elif command == 'deleteLast':
        li.pop()  # 末尾を削除

print(*li)
