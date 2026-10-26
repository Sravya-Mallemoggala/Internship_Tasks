# 20
# https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if stack:
        return ''.join(stack)
    else:
        return "Empty String"


s = input().strip()
print(superReducedString(s))