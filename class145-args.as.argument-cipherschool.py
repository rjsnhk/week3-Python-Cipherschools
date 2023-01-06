def multi(*args):
    m=1
    for i in args:
        m*=i
    print(args)
    print(m)
# multi(1,2,3)

num=[1,2,3,4]
multi(num)  #[1, 2, 3, 4] full list pack se 1 mulitiply hoga
multi(*num) #24  -- unpack ho jaega

n2=(2,3,3)
multi(*n2)  #18