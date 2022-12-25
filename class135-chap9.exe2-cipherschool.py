l=[True,'girl',[1,2,3],2, 4.0, 2.3, 7]
# output only int float convertto string
# x=[]
# for i in l:
#     if type(i)==int or type(i)==float:
#         x.append(str(i))
# print(x)

# string confresion
out=[str(i) for i in l if type(i)==int or type(i)==float]
print(out)