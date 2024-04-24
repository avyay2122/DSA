def MinStack():
    stack = []  
    min_stack = []
    
    def push(val):
        nonlocal stack, min_stack
        stack.append(val)
        if not min_stack or val <= min_stack[-1]:
            min_stack.append(val)

    def pop():
        nonlocal stack, min_stack
        if not stack:
            return None
        val = stack.pop()
        if val == min_stack[-1]:
            min_stack.pop()
        return val

    def top():
        if not stack:
            return None
        return stack[-1]

    def getMin():
        if not min_stack:
            return None
        return min_stack[-1]

    return push, pop, top, getMin


minStack_push, minStack_pop, minStack_top, minStack_getMin = MinStack()
minStack_push(-2)
minStack_push(0)
minStack_push(-3)
print(minStack_getMin())  
minStack_pop()
print(minStack_top())  
print(minStack_getMin())  
