l=['abc','def','ghi','jkl']
# reverse using loop
# rev=[]
# for i in l:
#     rev.append(i[::-1])
# print(rev)

# reverse using list comprehension
reverse=[j[::-1] for j  in l]
print(reverse)