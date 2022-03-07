l=[1,2,3,4,5]
x= 2
for  y in l:
    if(y == x):
        print("true",x)


if x in l :
    print("True",x)
    print(id(x))
    print(id(l[1]))