def greet():
    print("hello")

def fun(f):
    print("*"*10)
    f()
    print("*"*10)
fun(greet)