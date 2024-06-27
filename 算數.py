def postfix(expression):
    stack = []
    for num in expression.split():
        if num.isdigit():
            stack.append(int(num))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if num == '+':
                result = operand1 + operand2
            elif num == '-':
                result = operand1 - operand2
            elif num == '*':
                result = operand1 * operand2
            elif num == '/':
                result = operand1 // operand2
            elif num == '%':
                result = operand1 % operand2
            stack.append(result)
    return stack[0]
M= input()
print(postfix(M))



