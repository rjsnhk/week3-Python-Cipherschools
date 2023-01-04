def multi(*args):
    s=1
    for i in args:
        s*=i
    print(s)
multi(1,2,3)