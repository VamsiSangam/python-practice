class Person:
    'Base class for any person'

    def __init__(self, name):
        print('Inside Person class constructor')
        self.name = name    # instance variable

    def introduceYourself(self):
        print('Hi! I am ' + self.name + '!')

    def howManyLegs():
        return 2

    def howManyHands():
        return 2

class Employee(Person):
    'Optional class documentation string'
    empCount = 0    # class variable

    def __init__(self, name, salary):
        super().__init__(name)  # call to super class constructor
        self.salary = salary    # instance variable
        self.__secret = 'Shhh!' # can only be accessed inside class - Data Hiding
        Employee.empCount += 1  # class variable is accessed by class name

    def introduceYourself(self):    # overrides, but calls super class method
        super().introduceYourself()
        print('I am an employee and I earn $' + str(self.salary))

    def displayCount(self):
        print('Number of employees is - ' + str(Employee.empCount))

    def displayEmployeeDetails(self):
        print('Employee name - ' + self.name)
        print('Employee salary - ' + self.salary)

class Doctor(Person):
    'Documentation string for Doctor class'

    def __init__(self, name, hospital):
        super().__init__(name)
        self.hospital = hospital

    def introduceYourself(self):    # overriding method
        print('Hi! I am ' + self.name + ', and I am a Doctor!')
        print('I work in ' + self.hospital)

def main():
    person = Person('Guido van Rossum')
    employee = Employee('Bill Gates', 999999)
    doctor = Doctor('Hippocrates', 'Greek Hospital')

    print(person.name)                  # accessing instance variable
    person.introduceYourself()          # calling instance method

    # You can call an instance method by class name
    # but you'd have to supply the 'self' parameter
    Person.introduceYourself(person)
    print(Person.howManyHands())    # proper way of calling class method
    
    # print(person.howManyLegs())   # syntactically correct
    # but python supplies 'self' argument automatically, so this gives runtime error
    # TypeError: howManyLegs() takes 0 positional arguments but 1 was given

    employee.introduceYourself()
    doctor.introduceYourself()

main()