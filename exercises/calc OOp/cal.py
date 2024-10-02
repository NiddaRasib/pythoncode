'''
calc class
'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_two(self):
        return f"The sum is {self.num1 + self.num2}"   
    
    def subtract_two(self):
        return f"The difference is {self.num1 - self.num2}"
        
    def multiply_two(self):
        return f"The multiplication is {self.num1 * self.num2}"     
    
    def divide_two(self):
        return f"The division is {self.num1 / self.num2}"   

y = 0
while retry ==0: 

    print("\n welcome to calculator app \n")
    print("============================")
        
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("============================")

    print(f"+ : add")
    print(f"- : subtraction")
    print(f"* : multiply")
    print(f"/ : divide")
    ops = input("what type of operation do you want to perform? ")

    #create instance of a class
    calc = Calculator(num1, num2)

    if ops == "+":
        print(calc.add_two())
        retry = int(input(" Would you like to perform another calculation?\n 0 for Yes: \n 1 for No: "))
        if retry == 1:
            retry == 1
            break
        
    elif ops == "-":
        print(calc.subtract_two())
        retry = int(input(" Would you like to perform another calculation?\n 0 for Yes: \n 1 for No: "))
        if retry == 1:
            retry == 1
            break

    elif ops == "*":
        print(calc.multiply_two())
        retry = int(input(" Would you like to perform another calculation?\n 0 for Yes: \n 1 for No: "))
        if retry == 1:
            retry == 1
            break

    elif ops == "/":
        print(calc.divide_two())
        retry = int(input(" Would you like to perform another calculation?\n 0 for Yes: \n 1 for No: "))
        if retry == 1:
            retry == 1
            break

    else:
        print("Invalid operator")

    