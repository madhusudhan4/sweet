def wrapper(task,*args,**kwargs):
    print("*"*30)
    task(*args,**kwargs)
    print("*"*30)
def add(x,y):
    print(x+y)
def sub(a,b):
    print(a-b)

wrapper(add,2,3)
wrapper(sub,5,2)


