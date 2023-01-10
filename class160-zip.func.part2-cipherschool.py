# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l=[(1, 5), (2, 6), (3, 7), (4, 8)]
# print(list(zip(*l)))
# print(list(zip(l1,l2)))

# l=[(1, 5), (2, 6), (3, 7), (4, 8)]
# print(list(zip(*l)))
# a,b=zip(*l)
# print(list(a))
# print(list(b))


# pair me jo maximum number hoga
l1=[1,2,3,4,9]
l2=[5,6,7,8,4]
m=[]
for pair in zip(l1,l2):
    m.append(max(pair))
print(m)