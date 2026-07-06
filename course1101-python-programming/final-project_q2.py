str = input()
for c in str:
    print(c, ": ", end="", sep="")
    for i in range(int(c)):
        print(c, end="")
    print()