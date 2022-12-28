# dict compre
# output---square={1:1,2:2,3:3}

# sq={}
# for i in range(1,4):
#     sq[i]=i**2
# print(sq)

# dict compre.
# sq={num:num**2 for num in range(1,4)}
# print(sq)

# sq={f'square of {num} is':num**2 for num in range(1,4)}
# # print(sq)
# for k,v in sq.items():
#     print(f'{k}:{v}')
    

char='Rajeshhhssr'
# w_count={char[i]:char.count(char[i]) for i in range (len(char)) }
w_count={i:char.count(i) for i in char }
print(w_count)