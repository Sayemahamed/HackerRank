def main():
    s = input().strip()
    print(s.isalnum())
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


if __name__ == "__main__":
    main()
