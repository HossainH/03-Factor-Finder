def factor_finder(numbertofactor):
    factors = []
    for factor in range(1, numbertofactor + 1):
        if numbertofactor % factor == 0:
            factors.append(factor)

    print(f"All factors of {numbertofactor}: {factors}")

    if len(factors) == 1:
        print("Fun Fact! The number 1 is Unity, because it can only be divided by itself.")
    elif len(factors) == 2:
        print("This is a prime number!")
    else:
        print("This is a composite number")

numbertofactor = int(input("Enter a number between 1 and 200: "))
factor_finder(numbertofactor)
