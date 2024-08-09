def main():
    n = float(input("Please, input how many numbers you want to sum: "))
    floatCheck(n)
    n = int(n)

    oddSum, evenSum = oddAndEvenSum(n)

    print("\nThe sum of all odd numbers from 1 to", n, "is: ", oddSum)
    print("The sum of all even numbers from 1 to", n, "is: ", evenSum)
    print("The sum of all numbers from 1 to", n, "is: ", oddSum + evenSum)

def oddAndEvenSum(x):
    oddSum = 0
    evenSum = 0

    for i in range (1, int(x + 1)):
        if i % 2 == 0:
            evenSum += i
        if i % 2 != 0:
            oddSum += i

    return oddSum, evenSum

def floatCheck(x):
    while x % 1 != 0:
        x = float(input("Input not valid. Please, choose a valid number for the range for the sums: "))


if __name__ == "__main__":
    main()