# def multi(*args):
#     m=1
#     for i in args:
#         m*=i
#     print(m)
# multi(2,3,4) #24


# def multi(num,*args):
#     m=1
#     for i in args:
#         m*=i
#     print(m)
#     print(num)  #2
#     print(args)  #3,4
# multi(2,3,4) #12


# def multi(*args):
#     m=1
#     for i in args:
#         m*=i
#     print(m)
# multi()  #1


# def multi(num,*args):
#     m=1
#     for i in args:
#         m*=i
#     print(m)
# multi()  #error  --- *args ke bdle age jo bhi parameter hoga uske liye niche call ke time pe value lena padega  



# def multi(num1,num2,*args):
#     m=1
#     for i in args:
#         m*=i
#     # print(num1) #1
#     # print(num2) #2
#     # print(args) #()
#     print(m)
# multi(1,2) #none



# def multi(n1,n2,*args):
#     m=1
#     for i in args:
#         m*=i
#     print(m)    #12
#     print(n1)
#     print(n2)
#     print(args)
# multi(1,2,3,4)



# def multi(*args,n1):
#     m=1
#     for i in args:
#         m*=i
#     print(m)    
# multi(1,2,3,4)  #error -- pehle *args nhi hoga
