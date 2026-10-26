# 8
# https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common &= set(rock)

    return len(common)


n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

print(gemstones(arr))

