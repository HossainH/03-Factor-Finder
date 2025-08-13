def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")
    print('''
  Instructions:
- You will be asked to enter a number between or equal to 1 and 200
- If a valid input is taken, then the program will show you the factors of that number
- To exit the program, type 'xxx' when it asks for the input.

It is so simple it may as well be magic, Anyways, hope you find it useful :)
    ''')


def number_validity_and_exit():


    while True:
        exitcode = input("Type xxx if you would like to exit at this stage or enter to continue:  ")

        if exitcode == "xxx":
            print(""
                  "")
            return None

        try:
            response = int(input("Enter a number between or equal to 1 and 200: "))
        except ValueError:
            print("Oops, that's not a valid input, please enter an integer. Try again! ")
            continue

        if response > 200:
            print("The number entered is more than 200")
        elif response < 1:
            print("The number entered is less than 1")
        else:
            print("Thanks for the number, time to work magic :D")
            return response  # Return the valid number if it's within range.


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


def perf_sqrt_finder(numbertosqrt):
    for square in range(1, numbertosqrt + 1):
        if square * square == numbertosqrt:
            print(f"This number is also a perfect square of {square}!")
            return
        elif square * square > numbertosqrt:
            break
    print("Sadly this number is not a perfect square :(")


# Main program routine

want_instructions = input("Press <enter> to read the instructions or any key, then enter to continue: ")
if want_instructions == "":
    instructions()

while True:
    print(
        "Welcome to the factor calculator! If you wish to use it, just press enter and move on! \nBut if you happen to want to exit, type 'xxx', and we will sadly close for you.")
    number = number_validity_and_exit()
    if number is None:
        print("Thanks for visiting! Hope to see you soon. Exiting the program... Goodbye!")
        break
    else:
        factor_finder(number)
        perf_sqrt_finder(number)
        print()  # Blank line before next iteration


