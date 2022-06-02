def valid_parenthesis(s):
    stack=[]
    for char in s:
        if char in ['{','(','[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char=='{':
                if char!='}':
                    return False
            if current_char=='(':
                if char!=')':
                    return False
            if current_char=='[':
                if char!=']':
                    return False

    #check empty stack
    if stack:
        return False
    return True


if valid_parenthesis("()[]{}"):
    print("Balanced")
else:
    print("Not Balanced")