# class variable
# circle
# area
# circum
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumference(self):
        return 2*Circle.pi*self.radius


c = Circle(4)
c1 = Circle(5)
print(c1.calc_circumference())

class Laptop:
    discount_percent = 10
    def __init__(self, brand, model_name, price):
        #instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name
    
    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price



laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'mackbook pro', 230000)
print(laptop2.apply_discount())