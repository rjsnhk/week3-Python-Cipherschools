# def func(*args):
#     for i in args:
#         print (i[0].upper()+i[1::])
# name=['raj','nahak']
# func(*name)

def func(args,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in args]
    else:
        return [name.title() for name in args]
name=['rajesh','nahak','ram']

# print(func(name))
# print(func(name ,reverse_str=True))