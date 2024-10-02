'''
Calc Class
'''
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def add_two(self):
        return f'The sum is {self.num1 + self.num2}'
    
    def sub_two(self):
        return f'The difference is {self.num1 - self.num2}'
    
    def div_two(self):
        return f'The division is {self.num1 / self.num2}'
    
    def mul_two(self):
        return f'The multiplication is {self.num1 * self.num2}'

retry = 0
while retry ==0:
    print(f'Welcome to Calculator APP \n')
    print('====================================')
    num1 = int(input('Enter First Number : '))
    num2 = int(input('Enter Second Number : '))
    print('====================================')
    print(f'+ : addition')
    print(f'- : subraction')
    print(f'/ : division')
    print(f'* : multiplication\n')
    ops = input('What type of operation do you want to perform?:  ')
    print('====================================') 
    # create instance of class
    calc = Calculator(num1, num2)
    if ops == '+':
        print(calc.add_two())
        retry = int(input(' Would you like to perform another calculation\n0 for Yes: \n 1 for No: '))
        if retry == 1:
            retry == 1
            break
    
    elif ops == '-':
        print(calc.sub_two())
        retry = int(input(' Would you like to perform another calculation\n0 for Yes: \n 1 for No: '))
        if retry == 1:
            retry == 1
            break
    elif ops == '/':
        print(calc.div_two())
        retry = int(input(' Would you like to perform another calculation\n0 for Yes: \n 1 for No: '))
        if retry == 1:
            retry == 1
            break
    elif ops == '*':
        print(calc.mul_two())
        retry = int(input(' Would you like to perform another calculation\n0 for Yes: \n 1 for No: '))
        if retry == 1:
            retry == 1
            break