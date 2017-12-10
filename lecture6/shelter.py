class Animal(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

class Cat(Animal):
    def meow(self):
        return "meow"

class Dog(Animal):
    def bark(self):
        return "wuff, wuff"
