 #square
for i in range(9):
    for j in range (9):
        print("*",end=" ")
    print()

##right triangle
for i in range(9):
    for j in range(i+1):
        print("*",end=" ")
    print()

##inverse right triangle
for i in range(9,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

##pyramid
for i in range(6):
    for j in range(6-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()



##halow prymid:
def hollow_pyramid(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i or i == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
hollow_pyramid(5)


##inverse pyramid
rows = 3 
for i in range(rows):
    line = ' ' * i + '* ' * (rows - i)
    print(line)


##hallow square:
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



##hallow right triangle
rows = 5  
for i in range(1, rows + 1):
    row = []
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            row.append("*")
        else:
            row.append(" ")
    print(' '.join(row))

def print_diamond(n):
    # Upper half
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower half
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
print_diamond(5)
