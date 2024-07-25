#fibonnaci series
n=int(input("Enter a number: "))
def fibonacci_generator(n):
    if n <= 0:
        print("Enter a positive number")
    elif n == 1:
        print(0)
    elif n == 2:
        print(0)
        print(1)
    else:
        first = 0
        second = 1
        print(first)
        print(second)
        for i in range(2, n):
            third = first + second
            print(third)
            first = second
            second = third
fibonacci_generator(n)




