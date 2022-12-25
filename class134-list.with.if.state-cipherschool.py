num=list(range(1,10))

# even choose
# ev=[]
# for i in num:
#     if i%2==0:
#         ev.append(i)
# print(ev)

# list comprehsion
even=[i for i in num if i%2==0]
print(even)
even2=[i for i in range(1,16) if i%2==0]
print(even2)


odd=[i for i in num if i%2!=0]
print(odd)
odd3=[i for i in range(1,30) if i%2!=0]
print(odd3)