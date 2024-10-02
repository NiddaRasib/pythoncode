from main import Calculator

class MulTable(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def table(self):
        total = self.num1 + self.num2
        print(f" Sum of {self.num1} and {self.num2} = {self.add_two()}")
        for i in range(1,11):
            print(f"{total} * {i} = {total * i}")


class MulTable1(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)


    def table(self):
        total = self.num1 - self.num2
        print(f" Sum of {self.num1} and {self.num2} = {self.sub_two()}")
        for i in range(1,11):
            print(f"{total} * {i} = {total * i}")


#create instance of class
x = MulTable(3,5)
x = MulTable1(4,8)

#print multible
print(x.table())





