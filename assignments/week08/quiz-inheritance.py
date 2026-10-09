""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:

    def __init__(self, branf, model, year):
        self.brand = branf 
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):

    def __init__(self,brand, model, year):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number number of Doors: {self.number_of_doors}"
    