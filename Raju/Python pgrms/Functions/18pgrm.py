g = 9.8
def fun(n):
    x = 10
    y = 20
    n*=6
    print("----locala()------")
    print(locals())
    print("___globals()_____")
    print(globals())
def start():
    x = 50
    n = 7
    fun(n)
    print("__local___")
    print(locals())
    print("___globals___")
    print(globals())
start()
