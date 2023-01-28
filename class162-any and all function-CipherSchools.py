# any , all function

numbers1 = [13,1,9,7,10]
numbers2 = [1,2,3,4,5,6]

print(any([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers1]))

# evens1 = []
# for num in numbers1:
    # evens1.append(num%2==0)

# print(all([True, False, True, True])) #----> False
