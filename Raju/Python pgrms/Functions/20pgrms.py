g = 9.8
def fun3(x):
    print("fun3 start")
    print("stack frame of fun3:",locals())
    print("fun3 end")
def fun2(n):
    print("fun2 start")
    y=10
    n=n+1
    print("stack frame of fun2:",locals())
    fun3(n)
    print("fun2 end")
def fun1(n):
    print("fun1 start")
    n=n+1
    x=20
    print("satck frame of fun1:",locals())
    fun2(n)
    print("fun1 end")
def main():
    print("main start")
    a=15
    b=30
    print("stack frame of main:",locals())
    fun1(a)
    print("main end")

# if '__name__' == '__main__':
#  main()
# print(main())
main()