elements=input().split()
stack=[]
for element in elements:
    if element.isdigit():
        stack.append(int(element))
    elif element in '+-*':
        b = stack.pop()
        a = stack.pop()
        if element == '+':
            stack.append(a+b)
        elif element == '-':
            stack.append(a-b)
        elif element == '*':
            stack.append(a*b)
print(*stack)
