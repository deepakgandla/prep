from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

class Rectangle(Shape):
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth

	def area(self):
		return self.length * self.breadth

class Circle(Shape):
	def __init__(self, r):
		self.radius = r

	def area(self):
		return 3.1410 * self.radius * self.radius


rec = Rectangle(4, 3)
print(rec.area())
cir = Circle(4)
print(cir.area())