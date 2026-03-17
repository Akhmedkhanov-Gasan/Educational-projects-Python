def valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:

        if char not in pairs:
            stack.append(char)
        else:
            if stack == []:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack
