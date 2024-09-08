def main():
    input_count = int(input().strip())
    Names = set()
    for _ in range(input_count):
        Names.add(input().strip())
    print(len(Names))


if __name__ == "__main__":
    main()
