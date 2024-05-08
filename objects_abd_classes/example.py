class Person:

    def __init__(self, first_name, second_name, age=0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def say_hello(self):
        return f"Hello {self.first_name} are you {self.age}?"


person1 = Person("Tom", "Anderson", 21)
person2 = Person("Adam", "Kaley", 32)
person3 = Person("John", "Thomas", 53)


print(person1.say_hello())
