def main():
    p = float(input("\nPlease, input the number you want to check its perfection: "))
    floatCheck(p)

    perfectCheck(p)

    a = input("What would you like to do next?: \nC: Check another number \nX: Exit program \n")

    while a.upper() != 'C' and a.upper() != 'X':
        a = input("\nResponse not allowed. Please select a valid character: ")
        if a.upper() == 'C' or a.upper() == 'X':
            break

    if a.upper() == "C":
        main()

    if a.upper() == "X":
        print("\nUntil next time!")

def perfectCheck (n):
    sumDiv = 1
    mulDiv = 1

    for i in range (2, int(n)):
        if n % i == 0:
            sumDiv += i
            mulDiv *= i

    if n % 1 == 0:
        n = int(n)

    if sumDiv == mulDiv:
        return print(n, "is a perfect number!")

    else:
        return print(n, "is not a perfect number")

def floatCheck(n):
    while n % 1 != 0:
        n = float(input("Input not valid. Please, choose a valid number for the perfection check: "))


if __name__ == "__main__":
    main()