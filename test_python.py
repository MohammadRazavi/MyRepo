class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'His age is {self.age} and his name is {self.name}')

name_id = Name("Mohammad",14)
print(name_id.display_info())

print('hello')