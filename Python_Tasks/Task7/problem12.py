# 12
# https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)

    return sum(abs(c1[ch] - c2[ch]) for ch in set(c1) | set(c2))

s1 = input().strip()
s2 = input().strip()

print(makingAnagrams(s1, s2))