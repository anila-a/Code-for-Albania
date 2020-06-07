'''
Last date modified: 05/25/2020

Provide the implementation of the GeometricShape class with two attributes: color and filled. 
Set color = ‘black’ and filled = False as default. Write the getter and setter methods for each attribute.

Implement three other classes: Rectangle and Circle, which inherit from the GeometricShape class, 
and Square, which inherits from the Rectangle class. Add the specified attributes and methods for each subclass 
as shown in the class diagram. Test each class.
'''

import math

class GeometricShape:

  # Constructor
  def __init__(self, color = 'black', filled = False):
    self.color = color
    self.filled = filled

  # Getters and setters
  def get_color(self):
    return self.color

  def set_color(self, color):
    self.color = color

  def get_filled(self):
    return self.filled

  def set_filled(self, filled):
    self.filled = filled

class Rectangle(GeometricShape):

  # Constructor
  def __init__(self, length, breadth):
    super().__init__()
    self.length = length
    self.breadth = breadth
  # Getters and setters
  def get_length(self):
    return self.length

  def set_length(self, length):
    self.length = length

  def get_breadth(self):
    return self.breadth

  def set_breadth(self, breadth):
    self.breadth = breadth
  # get_perimeter()
  def get_perimeter(self):
    return 2 * (self.length + self.breadth)
  # get_area()
  def get_area(self):
    return self.length * self.breadth

class Circle(GeometricShape):

  # Constructor
  def __init__(self, radius):
    super().__init__()
    self.radius = radius
  # Getter and setter
  def get_radius(self):
    return self.radius

  def set_radius(self, radius):
    self.radius = radius
  # get_perimeter()
  def get_perimeter(self):
    return 2 * math.pi * self.radius
  # get_area()
  def get_area(self):
    return math.pi * pow(self.radius, 2)

class Square(Rectangle):
  pass

# Main function

r = Rectangle(10.5, 12.5)

print('Area of rectangle:', r.get_area())
print('Perimeter of rectangle:', r.get_perimeter())
# Is the rectangle filled?
print(r.get_filled())
r.set_color('blue')
print(r.get_color())

# Create a circle object

# Print the area of circle
# Print the perimeter of circle
# Print the color of circle

# Create a square object
s = Square(5, 5)
# Print the area of square
print(s.get_area())
# Print the perimeter of square
# Print the color of square
# Is the rectangle filled?
