def number_validity():
    print(
        "Welcome to the factor calculator! If you wish to use it, just press enter and move on! \nBut if you happen to want to exit, type 'xxx', and we will sadly close for you.")

    while True:
        exitcode = input("Type your choice: ")

        if exitcode == "xxx":
            print("Thanks for visiting! Hope to see you soon.")
            return None

        try:
            response = int(input("Enter a number between or equal to 1 and 200: "))
        except ValueError:
            print("Oops, that's not a valid number! Try again.")
            continue

        if response > 200:
            print("The number entered is more than 200")
        elif response < 1:
            print("The number entered is less than 1")
        else:
            print("Thanks for the number, time to work magic :D")
            return response  # Return the valid number if it's within range.


number_validity()