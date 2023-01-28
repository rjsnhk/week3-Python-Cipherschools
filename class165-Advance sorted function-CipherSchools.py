fruits = ['grapes', 'mango', 'apple']
# sort
# fruits.sort()
# print(fruits)

fruits2 = ('grapes', 'mango', 'apple')
# print(sorted(fruits))


fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits))



guitars = [
    {'model': 'yamaha f310','price':8400},
    {'model': 'faith naptune','price':50000},
    {'model': 'faith apollo venus','price':35000},
    {'model': 'taylor 814ce','price':450000}
]

sorted_guitars = sorted(guitars, key = lambda d:d['price'], reverse = True)
print(sorted_guitars)