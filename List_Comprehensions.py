def main():
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    number= int(input().strip())
    ans=[]
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i+j+k!=number:
                    ans.append([i,j,k])
    print(ans)

if __name__ == '__main__':
    main()
