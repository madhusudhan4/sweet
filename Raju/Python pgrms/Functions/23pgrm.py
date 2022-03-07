def fun(*args):
    s=0
    a=len(args)
    for x in args:
        s +=x
    return s,a

a,s = fun(1,2,3,4,5)
print(s/a)