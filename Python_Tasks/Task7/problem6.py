# 6
# https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set()

    for ch in s.lower():
        if ch.isalpha():
            letters.add(ch)

    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))
