def fizzbuzz() -> None:
    n = int(input("Enter a number: "))
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 3 == 0:
            print("buzz")   
        else:
            print(i)      

fizzbuzz()


def fizz1buzz1(n : int) -> None:
    for x in range(n+1):
        if x % 5 == 0 and x % 3 == 0:
            print("Fizz1buzz1")
        elif x % 3 == 0:
            print("Fizz1")
        elif x % 5 == 0:
            print("buzz1")
        else:
            print(x)

fizz1buzz1(10)

