# LIST COMPREHENSION

# square=[i**2 for i in range(1,11)]
# print(square)

# if use in list comp
# even=[i for i in range(1,10) if i%2==0]
# print(even)

# # if else
# mix=[i*2 if i%2==0 else -i for i in range(1,10) ]
# print(mix)

# list inside list
mix=[[i for i in range(1,3)] for j in range(1,9)]
print(mix)
