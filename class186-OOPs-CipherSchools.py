# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD , CONSTRUCTOR
# WHAT ARE THE ATTRIBUTES , INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print('init method called')
        self.person_first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Harshit','Vashistha',24)
p2 = Person('Mohit', 'Vashistha', 19)

print(p1.person_first_name)
print(p2.person_first_name)

