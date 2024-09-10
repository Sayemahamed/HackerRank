from collections import OrderedDict


def main():
    n = int(input())
    dictionary = OrderedDict()
    for _ in range(n):
        temp = input().split()
        price = int(temp[-1])
        name = " ".join(temp[:-1])
        if name in dictionary:
            dictionary[name] += price
        else:
            dictionary[name] = price
    for key, value in dictionary.items():
        print(key, value)


if __name__ == "__main__":
    main()
