# 14
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2:
        return -1

    half = len(s) // 2
    return sum((Counter(s[:half]) - Counter(s[half:])).values())

q = int(input())

for _ in range(q):
    s = input().strip()
    print(anagram(s))