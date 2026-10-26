# 13
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(s)
    count_freq = Counter(freq.values())

    if len(count_freq) == 1:
        return "YES"

    if len(count_freq) > 2:
        return "NO"

    (a, fa), (b, fb) = sorted(count_freq.items())

    if a == 1 and fa == 1:
        return "YES"

    if b == a + 1 and fb == 1:
        return "YES"

    return "NO"

s = input().strip()
print(isValid(s))