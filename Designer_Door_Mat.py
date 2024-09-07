def main():
    x,y = map(int,input().strip().split())
    for i in range(1,x,2):
        print((".|."*i).center(y,"-" ))
    print("WELCOME".center(y,"-"))
    for i in range(x-2,0,-2):
        print((".|."*i).center(y,"-"))


if __name__ == "__main__":
    main()