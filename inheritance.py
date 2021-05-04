class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'Hai I am {self.name} and I am {self.age} years old')

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def show(self):
        print(f'Hai I am {self.name} and Iam {self.age} years old {self.color} in color')
    def speak(self):
        print('bow')

class Cat(Pet):
    def speak(self):
        print('Meow')

p = Pet('John', 19)
p.show()
d = Dog('Brandy', 5, 'Brown')
d.show()
c = Cat('Juicy', 5)
c.show()
d.speak()
c.speak()


