def main():
    x = float(input("Please, insert how many numbers would you like to check: "))
    floatCheck(x)

    numberList = []
    for i in range(0, int(x)):
        n = float(input("Please, enter a number: "))
        numberList.append(n)
    positiveList = positiveCheck(numberList)

    if len(positiveList) == 0:
        print("You've entered no positive numbers")
    else:
        print("The positive numbers are: ")
        for j in range(0, len(positiveList)):
            if positiveList[j] % 1 == 0:
                print(int(positiveList[j]))
            else:
                print(positiveList[j])

def positiveCheck(numbers):
    positiveNumbers = []
    for i in range(0, len(numbers)):
        if numbers[i] > 0:
            positiveNumbers.append(numbers[i])
    return positiveNumbers

def floatCheck(a):
    while a % 1 != 0:
        a = float(input("Input not valid. Please, choose a valid number for the range for the sums: "))


if __name__ == "__main__":
    main()