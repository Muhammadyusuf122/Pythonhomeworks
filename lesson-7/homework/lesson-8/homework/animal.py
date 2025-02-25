class Animal:
    
       

    def speak(self):
        return "sound"
    def eat(self):
        return "it is eating"
    def hunt(self):
        return "Hunting"
    


class Dog(Animal):
    def speak(self):
        return "Wooof!"
    def eat(self):
        return "bones"
    def hunt(self):
        return "Cats"
    

class Cat(Animal):
    def speak(self):
        return "Meow, meow"
    def eat(self):
        return 'mice'
    def hunt(self):
        return "mouse"
    

class Wolf(Animal):
    def speak(self):
        return 'avoooo'
    def eat(self):
        return "meat"
    def hunt(self):
        return "wild animals"
    pass


dog1 = Dog()
print(dog1.speak())
print(dog1.hunt())

cat1 = Cat()
print(cat1.speak())
print(cat1.eat())

wolf2 = Wolf()
print(wolf2.eat())