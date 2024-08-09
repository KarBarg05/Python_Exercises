def main():
    n = float(input("Please, input how many numbers you want to check: "))
    numberCheck(n)

    primeList = primeFinder(n)

    if len(primeList) == 1:
        return print("Seriously? Number 1 does not count as a prime -_-")
    if len(primeList) == 2:
        return print("Yeah yeah, number 2 is a prime. In fact, it's the smallest one!")
    if len(primeList) > 2:
        print("The primes until", n, "are: \n")
        for i in range (0, len(primeList)):
            print(primeList[i])

def primeFinder(x):
    primes = []

    for i in range (1, int(x + 1)):
        div = []
        for j in range (1, i):
            if i % j == 0:
                div.append(j)
        if len(div) == 2:
            primes.append(i)

        return primes

def numberCheck(n):
    floatCheck(n)
    positiveCheck(n)

def positiveCheck(x):
    while x <= 0:
        x = float(input("Input not valid. Please, choose a valid POSITIVE number for the range for the primes: "))
        if x % 1 != 0:
            floatCheck(x)

def floatCheck(x):
    while x % 1 != 0:
        x = float(input("Input not valid. Please, choose a valid NON-DECIMAL number for the range for the primes: "))
        if x <= 0:
            positiveCheck(x)


if __name__ == "__main__":
    main()