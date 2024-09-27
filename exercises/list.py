# list in dictionary

person = {
    "Name": "NiddaRasib",
    "Program": "Software Engineering",
    "Courses": ['Advanced Programming', 'Application Development', 'Algorithm and Data Structures'],
    "Grades": ['A', 'B', 'C']
    
}

Grades = person.get('Grades')
print (Grades) # ['A', 'B', 'C']

print(type(Grades)) #<class 'list'>

for grade in Grades:
    if grade == 'A':
        print('Grade is A') #Grade is A


# function without parameter

def func1():
    return 2+2
print(func1)

#function with argument
def square(x:int) -> int:
    result = x*x
    return result  # <function func1 at 0x000001A025554C20>

def getEven(n:int) -> None:
    for i in range(n+1):
        if i % 2 == 0:
            print('Even')
        else:
            print(i)

#call the function
getEven(5)
getEven(6)


def prompt():
    name = input('Enter Name:')
    location = input('Enter City:')
    return name, location

def greet():
    
#call prompt()
    name, location = prompt()
    print(f'Welcome {name} \nHow is {location} today?')

greet()

#Enter Name:Nidda
#Enter City:Bradford
#Welcome Nidda
#How is Bradford today?

