def main():
    n = float(input("Please, insert how many numbers would you like to check: "))
    floatCheck(n)

    numbers = []
    for i in range(0, int(n)):
        m = float(input("Please enter a number: "))
        numbers.append(m)

    greatestNumber(numbers)

def greatestNumber(numList):
    greatestNum = numList[0]
    for i in range(0, len(numList)):
        if greatestNum < numList[i]:
            greatestNum = numList[i]

    if greatestNum % 1 == 0:
        print("The greatest number is:", int(greatestNum))
    else:
        print("The greatest number is:", greatestNum)

def floatCheck(a):
    while a % 1 != 0:
        a = float(input("Input not valid. Please, choose a valid number for the range for the sums: "))


if __name__ == "__main__":
    main()