import math

def add(*args):
    print(sum(args))

def sub(*args):
    print(math.prod(args))

def shedular(task, *args, **kwargs):
    task(*args,**kwargs)

shedular(add,2, 3)
shedular(add, 5, 6, 3, 4)
shedular(sub,1,2,3)
