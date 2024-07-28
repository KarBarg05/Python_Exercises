def main():
    n = float(input("Please input the number of elements you want to check their squares (please, put more than 5): "))
    numberCheck(n)
    n = int(n + 1)

    squareList = []
    for i in range (1, n):
        s = squareMaker(i)
        squareList.append(s)

    print("The squares are: ")
    output = ""
    for j in range (6, n):
        output += str(squareList[j - 1])
        if j < n - 1:
            output += ", "
    print(output)

def squareMaker(x):
    return x*x

def numberCheck(x):
    while x <= 5:
        x = float(input("Please input the number of elements you want to check, and PLEASE put more than 5: "))
        numberCheck(x)
    while x % 1 != 0:
        x = float(input("Please input the NON-DECIMAL number of elements you want to check (remember, more than 5): "))
        numberCheck(x)

if __name__ == "__main__":
    main()