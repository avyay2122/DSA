def sol(l1,l2):
    m = []
    carry = 0
    max_len = max(len(l1),len(l2))
    
    for i in range(max_len):
        num1 = l1[i] if i < len(l1) else 0
        num2 = l2[i] if i < len(l2) else 0
        
        sum1 = num1 + num2 + carry
        m.append(sum1%10)
        carry = sum1 // 10
    if carry > 0:
        m.append(carry)
    return m
l1 = [2,4,3]
l2 = [5,6,4]
print(sol(l1,l2))
