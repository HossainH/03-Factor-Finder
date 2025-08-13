def perf_sqrt_finder(numbertosqrt):
    for square in range(1, numbertosqrt + 1):
        if square * square == numbertosqrt:
            print(f"This number is also a perfect square of {square}!")
            return
        elif square * square > numbertosqrt:
            break
    print("Sadly this number is not a perfect square :(")