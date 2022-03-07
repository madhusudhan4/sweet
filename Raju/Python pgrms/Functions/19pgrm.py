g = 9.8
def fun():
    global g
    g=12
def start():
    print("before fun():",g)
    fun()
    print("after fun():",g)
start()