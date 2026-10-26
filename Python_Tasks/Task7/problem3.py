# 3
# https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    count = 0

    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2:  # Expected 'S'
            if s[i] != 'S':
                count += 1
        else:  # Expected 'O'
            if s[i] != 'O':
                count += 1

    return count


if __name__ == '__main__':
    s = input().strip()
    print(marsExploration(s))