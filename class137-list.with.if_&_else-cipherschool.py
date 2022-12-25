num=list(range(1,15))
# # out if ev=2*2,4*2 odd=-1,-3
# l=[]
# for i in num:
#     if i%2==0:
#         l.append(i*2)
#     else:
#         l.append(-i)
# print(l)

# list comprehasion
new2=[i*2 if i%2==0 else -i for i in num ]
print(new2)