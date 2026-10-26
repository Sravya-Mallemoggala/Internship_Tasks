# 17
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = int(s[:i])

        temp = str(first)
        nxt = first + 1

        while len(temp) < n:
            temp += str(nxt)
            nxt += 1

        if temp == s:
            print("YES", first)
            return

    print("NO")

q = int(input())

for _ in range(q):
    separateNumbers(input().strip())