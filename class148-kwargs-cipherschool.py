# kwargS as parameter

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))  #dict
# func(fname='rajesh',lname='nahak') #out---{'fname': 'rajesh', 'lname': 'nahak'}


# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# func(fname='rajesh',lname='nahak')

# # out --fname:rajesh
# #       lname:nahak

def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
d ={'name':'raj','age':19,'movie':'beast'}
func(**d)  #for unpack
# out ---
# name:raj
# age:19
# movie:beast