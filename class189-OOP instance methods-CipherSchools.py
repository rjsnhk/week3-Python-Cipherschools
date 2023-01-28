# instance methods
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)
print(p1.is_above_18())
# print(p2.full_name())

# l = [1,2,3]
# clear , pop 
# l.clear()
# list.clear(l)
# print(l)
# list.append(l,10)
# print(l)