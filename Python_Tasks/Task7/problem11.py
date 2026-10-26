# 11
# https://www.hackerrank.com/challenges/two-strings/problem

def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

q = int(input())

for _ in range(q):
    s1 = input().strip()
    s2 = input().strip()

    print(twoStrings(s1, s2))