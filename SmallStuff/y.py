class Person :
    def __init__(self, age, name):
       self.age = input("age?")
       self.name = input("name?")
user = Person(13, "Denis")
print(user.age)
print(user.name)
