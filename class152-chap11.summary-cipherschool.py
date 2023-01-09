# def add(a,b):
#     return(a+b)  #only for 2 parameter

def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
# add(2,3,4)

# n1=[1,2,3,4]
# add(*n1)

# n2=(1,2,3,4,5)
# add(*n2)

# kwargs==keyward argument ,**
def func(**kwargs):
    print(kwargs)
    
# func(name='raj',age=19)
d={'name':'raj','age':19}
func(**d)


# normal parameter , *args  ,  default para , **kwargs

# padk
def func2(name,*args,lname='unknown',**kwargs):
    print(name)
    print(args)
    print(lname)
    print(kwargs)
func2('rajesh',1,2,3,a=1,b=2,c=3)




