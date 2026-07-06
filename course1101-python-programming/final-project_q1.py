n = int(input())
mid = n//2

if n >= 1 and n <= 19:
    for row in range(n):
        if row <= mid:
            asterix = 2 * row + 1
        else:
            asterix = 2 * ( n - row - 1 ) + 1

        spaces = (n - asterix) // 2
        line = " " * spaces + "*" * asterix + " " * spaces
        
        print(line, line)