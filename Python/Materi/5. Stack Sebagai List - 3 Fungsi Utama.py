stack2 = []

def push2(item):
    stack2.append(item)

def pop2():
    return stack2.pop() if stack2 else None

def peek2():
    return stack2[-1] if stack2 else None
