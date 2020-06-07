'''
Last date modified: 05/23/2020

Exercise 1: Create the class Employee. The class constructor takes the following parameters:

Employee name
Position in the company: set as protected member
Monthly salary: set as private member

Create the display method to print out the data. Test the class.

Exercise 2: Create the abstract class Abstract. Define two methods:

display(): takes an integer as a parameter and prints its value
task(): abstract method, prints a statement

Create two subclasses, Test and Example, which inherit from Abstract class. Both subclasses must have their 
own task() method (extension of the abstract method). Test the classes and make a full code analysis.
'''

# Import ABC module
from abc import ABC, abstractmethod

# Class Employee
class Employee:

  # Constructor
  def __init__(self, name, position, salary):
    self.name = name
    self._position = position
    self.__salary = salary

  # Display method
  def display(self):
    print("Name:", self.name)
    print("Position:", self._position)
    print("Salary: $", self.__salary)

  # Getter and setter
  def get_salary(self):
    return self.__salary

  def set_salary(self, salary):
    self.__salary = salary


# Class Abstract
class Abstract(ABC):

    # Display method
    def display(self, x):
      print("Passed value:", x)

    # Abstract task method 
    @abstractmethod
    def task(self):
      pass

# Test class
class Test(Abstract):
  # Override 
  def task(self):
    print("we are inside test task.")

# Main method

# Create an instance of Employee class
e = Employee("Andi", "Software Engineer", 3000)

# Accessing using class method
e.display()

# Accessing from outside the class
print(e.name)
print(e._position)
e.set_salary(4000)
print(e.get_salary())

print()
# Create object from Test class and test it
test = Test()
test.task()
test.display(4)

# abs = Abstract()
# abs.task()
# abs.display(5)

# Is Test an instance of Abstract?
print("test is instance of Abstract class", isinstance(test, Abstract))
