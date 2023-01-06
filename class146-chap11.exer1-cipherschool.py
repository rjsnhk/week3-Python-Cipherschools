# def power(*args):
#     if len(num)!=0:
#         l=[]
#         for i in args:
#             l.append(i**3)
#         print(l)
#     else:
#         print('you did not pass any arg')
# num=[1,2,3,3]
# power(*num)


# list comprehension
def power(*args):
    if len(num)!=0:
        l=[i**3 for i in args]
        print(l)
    else:
        print('you did not pass any arg')
num=[1,2,3,3]
power(*num)


