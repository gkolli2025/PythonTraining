num=int(input("Enter a number: "))
for i in range(1, num+1):
    for j in range(num, i,-1):
        print(chr(i+64),end="")
    print()

