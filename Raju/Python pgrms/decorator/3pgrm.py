def stars(f):
    def wrapper(*args,**kwargs):
        print("*"*10)
        ret =f(*args,**kwargs)
        print("*"*10)
        # return ret
    return wrapper
@stars
def add(*args):
    print(sum(args))
add(2,3)
import math
@stars
def avg(*args):
    a=sum(args)/len(args)
    return a
avg(5,2,8)
add(5,7,6,8,9,5)
add(1)
print(avg(5,3,5))

