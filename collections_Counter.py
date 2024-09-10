from typing import Counter


def main():
    input()
    shoes = list(map(int, input().strip().split()))
    customers = int(input().strip())
    earned = 0
    shoes = Counter(shoes)
    for _ in range(customers):
        size, price = map(int, input().strip().split())
        if shoes[size]:
            earned += price
            shoes[size] -= 1
    print(earned)


if __name__ == "__main__":
    main()
