# out--{1:odd,2:even}
# l={}
# for i in range(4):
#     if i%2==0:
#         l[i]='even'
#     else:
#         l[i]='odd'
# print(l)

# dict comprehenssion
odd_even={i:('even' if i%2==0 else 'odd') for i in range(6)}
print(odd_even)