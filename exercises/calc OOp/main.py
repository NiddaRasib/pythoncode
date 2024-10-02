'''
calc class
'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add_two(self):
        return f"The sum is {self.num1 + self.num2}"
    
#create instance of a class

calc = Calculator(num1=5, num2=6) 

print(calc.add_two()) #The sum is 11