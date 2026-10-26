# 7
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3

    rows = []

    for i in range(size):
        s = "-".join(alpha[i:size])
        rows.append((s[::-1] + s[1:]).center(width, "-"))

    print("\n".join(rows[:0:-1] + rows))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)