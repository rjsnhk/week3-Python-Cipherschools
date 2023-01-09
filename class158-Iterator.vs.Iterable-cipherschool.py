num=[1,2,3,4,5,6] #tuple,string,list--iterable
sqr=(map(lambda a:a**2,num))  #map,filter--iterator
# print(sqr)
# for i in sqr:
#     print(i)
    
    
# nums=(iter(num))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# sqr already is a iter
print(next(sqr))
print(next(sqr))
print(next(sqr))