'''class Vehicles:
    def __init__(self, toyota, benz, mazda, volkswagon):
        self.toyota = ('brake', 'steering')
        self.benz = ('speed', 'classic')
        self.mazda = ('strength', 'chassis')
        self.volkswagon = ('durability', 'economical')'''
#
class Animal:
    def sound(self):
        return 'some generic animal sound'
    
class Dog(Animal):
    def sound(self): 
     return "woof!"
    
doggy = Dog()
print(doggy.sound())

class Animal:
   def __init__(self, name):
      self.name = name

   def sound(self):
      return "Some generic animal sound"
   
   class Dog(Animal):
      def __init__(self, name, breed):
         super().__init__(name)
         self.breed = breed

   class Cat(Animal):
      def __init__(self, name, color):
         super().__init__(name)
         self.color = color 

   class Goat(Animal):
      def __init__(self, name, fur):
         super().__init__(name)
         self.fur = fur 
      
    
print(name.dog)

'''
class ParentClass:

'''




'''
class Jkbrime:
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby

    def greetings(self):
        print(f'hello {self.name}')

    def greetings(self):
        print(f" i am {self.age} years old")

    def greetings(self):
        print(f" i am a {self.gender} ")
    
    def greetings(self):
        print(f"{self.hobby} is my hobby")

    def details(self):
        print("your gender is {} ".format(self.gender))
        print("your age is {} ".format(self.age))

greeting_shade = Jkbrime('shade', 40, 'female', 'watching_soccer')
print(greeting_shade.gender)
print(greeting_shade.name)
print(greeting_shade.age)
print(greeting_shade.hobby)
greeting_shade.greetings()
greeting_shade.details()
'''