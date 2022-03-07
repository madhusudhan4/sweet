g = 9.8
def fun3(n):
    global a
    a=29
    global b
    b=12
    global c
    c=100
    d=12973

    print("start fun3")
    print("local",locals())
    print("globals",globals())
def fun2(n):
    y = 23
    z = 25
    n = n+1
    print("start fun2")
    print("locals",locals())
    fun3(n)
    # print("globals",globals())
def fun1(n):
    a=13
    b=24
    n=n+1
    print("fun1 start")
    print("locals",locals())
    fun2(n)
    # print("globals",globals())

def main():
    f=10
    n=10
    print("start main")
    print("locals",locals())
    fun1(n)
    print("globals",globals())
# if "__name__" == "__main__":
main()