# Multiple Inheritance

class A:

    def class_a_methods(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'

class B:

    def class_a_methods(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'

class C(A,B):
    pass

instance_c = C()
# print(instance_c.class_a_methods())
# print(instance_c.class_b_methods())
# print(instance_c.hello())
# print(help(C))
# print(C.mro())
print(C.__mro__)
