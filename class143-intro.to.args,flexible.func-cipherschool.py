# make flexible func

# * operator
# *args

# def total(a,b):
#     print(a+b)
# # total(3,4)  #7
# total(3,4,5,6)  #error so use *operator

# jitne marji argument pass nhi ho pata so pass karane ke liye
def all_total(*args):
    # print(args)
    # print(type(args))
    sum=0
    for i in args:
        sum+=i
    print(sum)
all_total(2,4,5,6,7)
all_total(1,123,4,4,332,211,3,33,3332144)

