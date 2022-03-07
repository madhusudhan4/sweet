# parameter unpacking
d = {"x":10,"y":20,"z":30}
t = (1,2,3)
l = [4,5,6]
def fun(x,y,z):
    r=(x+y+z)
    return r
res = fun(d['x'],d['y'],d['z'])
print(res)
