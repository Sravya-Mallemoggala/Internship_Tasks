# 19
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()

    current_weight = 0
    prev = ''

    for ch in s:
        value = ord(ch) - ord('a') + 1

        if ch == prev:
            current_weight += value
        else:
            current_weight = value

        weights.add(current_weight)
        prev = ch

    return ["Yes" if q in weights else "No" for q in queries]


s = input().strip()

n = int(input())

queries = [int(input()) for _ in range(n)]

result = weightedUniformStrings(s, queries)

for ans in result:
    print(ans)
