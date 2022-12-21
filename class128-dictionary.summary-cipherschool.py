# d={'name':'raj','age':19,'movie':'jadugar'}
# print(d)


# d1=dict(name='raj',age=19,movie='jadugar')
# print(d1)

# d2={'name':'raj',
#    'age':19,
#    'movie':'jadugar'}
# print(d2)

# # print values
# print(d['name'])

d={}
d['name']='rajesh'
d['age']=19
# print(d)

# if 'name' in d:
#     print('true')
    
    
# if 'rajesh' in d.values():
#     print('true')

# for key,value in d.items():
#     print(f'key is {key} and value is {value}')

# # to print all key
# for i in d:
#     print(i)


# # to print all value
# for i in d.values():
#     print(i)

# # get method
# print(d.get('name'))  #rajesh
# print(d.get('names')) #None


# print(d['names']) #keyerror
# print(d.get('names')) #None


# popped=d.pop('name')
# print(popped)
# print(d)

popped=d.popitem()
print(popped)
print(d)



