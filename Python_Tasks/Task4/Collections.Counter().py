from collections import Counter

n = int(input())
shoes = list(map(int, input().split()))

inventory = Counter(shoes)

customers = int(input())
earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1

print(earnings)