M = int(input())
while M != 0:
    A = list(input())
    stack = []
    for char in A:
        if char in "([":  
            stack.append(char)
        elif char in ")]":  
            if stack and ((char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[")):
                stack.pop()  
            else:
                stack.append(char)  

    if not stack:
        print("VALID")
    else:
        print("NOT VALID")
    
    M -= 1
                