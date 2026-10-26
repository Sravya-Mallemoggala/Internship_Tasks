# 15
# https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    odd = sum(v % 2 for v in Counter(s).values())
    return "YES" if odd <= 1 else "NO"

s = input().strip()
print(gameOfThrones(s))