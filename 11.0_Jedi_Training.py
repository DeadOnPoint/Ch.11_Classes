'''
Sign your name:Will Jacobson
 
 1. Write code that defines a class named Animal:
     * Add a constructor for the Animal class that prints 'An animal has been born.'
     * Add an attribute for the animal name.
     * Add an eat() method for Animal that prints 'Munch munch.'
     * Add a make_noise() method for Animal that prints 'Grrr says [animal name].'

     
 2. Write code that defines a class named Cat:
     * Make Animal the parent.
     * Add a constructor for Cat that prints 'A cat has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Cat that prints 'Meow says [animal name].'

     
 3. Write code that defines a class named Dog:
     
     * Make Animal the parent.
     * Add a constructor for Dog that prints 'A dog has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Dog that prints 'Bark says [animal name].'

     
 4. Write a main program with:
     
     * Code that creates a cat, two dogs, and an animal with names.
     * Code that calls eat() and make_noise() for each animal.
     
 OUTPUT:
An animal has been born.
A cat has been born.
Munch munch
Meow says (cat name) .
An animal has been born.
A dog has been born.
Munch munch
Bark says (dog name).
An animal has been born.
A dog has been born.
Munch munch
Bark says (another dog name) .
An animal has been born.
Munch munch
Grrr says (animal name) .
'''

class Animal():
    def __init__(self, new_name):
        print("An animal has been born.")
        self.name = new_name

    def eat(self):
        print("Munch Munch")

    def make_noise(self,new_name):
        print("Grr says", new_name)

class Cat(Animal):
    def __init__(self, new_name):
        super().__init__(new_name)
        print("A cat has been born.")

    def eat(self):
        print("Munch Munch")

    def make_noise(self,new_name):
        print("Meow says", new_name)

class Dog(Animal):
    def __init__(self, new_name):
        super().__init__(new_name)
        print("A dog has been born.")

    def eat(self):
        print("Munch Munch")

    def make_noise(self,new_name):
        print("Bark says", new_name)

if __name__ == "__main__":
    cat = Cat("Leo")
    cat.eat()
    cat.make_noise("Leo")
    dog1 = Dog("Stacy")
    dog1.eat()
    dog1.make_noise("Stacy")
    dog2 = Dog("Charles")
    dog2.eat()
    dog2.make_noise("Charles")
    animal = Animal("Bear")
    animal.eat()
    animal.make_noise("Bear")
