def main():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    happy_ness = 0
    happy_set = set(map(int, input().split()))
    sad_set = set(map(int, input().split()))
    for i in array:
        if i in happy_set:
            happy_ness += 1
        elif i in sad_set:
            happy_ness -= 1
    print(happy_ness)


if __name__ == "__main__":
    main()
