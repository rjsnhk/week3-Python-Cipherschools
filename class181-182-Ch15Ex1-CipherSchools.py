def even_generator(n):
    for num in range(2,n+1,2):
        yield(num)

even_nums = even_generator(20)
for num in even_nums:
    print(num)