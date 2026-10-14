
from collections import Counter

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))

    shoe_count = Counter(shoe_sizes)

    N = int(input())
    total = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoe_count[size] > 0:
            total += price
            shoe_count[size] -= 1

    print(total)
