class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def read(self):
        print( f"i have read the {self.title} authored by {self.author}")

book1 = Book("cash flow quadrant"," Robert T kiyosaki")
book1.read()

class Vehicle:
    def move(self):
        print('Generic movement')
class Car(Vehicle): 
    def move(self):
        print('running')
class Plane(Vehicle):
      def move(self):
        print('flying')

car = Car()
plane = Plane()
    
car.move()
plane.move()