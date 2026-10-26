# 18
# https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    return len(set(s))

q = int(input())

for _ in range(q):
    s = input().strip()
    print(stringConstruction(s))
