# variable keyword arguements
def fun(**kwargs):
    print(type(kwargs))
    print(kwargs)
res = fun(a=20,b=21,c=67,d=23,e=12)
res = fun(a=20,y=21,z=67,)
print(res)