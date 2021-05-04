class Rectangle:
	def __init__(self, length, breadth):
		self.__length = length
		self.__breadth = breadth

	def get_length(self):
		return self.__length

	def set_length(self, value):
		self.__length = value

	def get_breadth(self):
		return self.__breadth

	def set_breadth(self, value):
		self.__breadth = value

	def area(self):
		return self.__length * self.__breadth

rec = Rectangle(10 ,20)
rec.set_length(1000)
print(rec.area())
print(rec.get_length())