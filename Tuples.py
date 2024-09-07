def main():
    input()
    arr = list(map(int, input().split(" ")))
    ans= tuple(arr)
    print(hash(ans))
if __name__ == '__main__':
    main()