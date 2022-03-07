t = 1,2,3
def fun(*args):
    # s=0
    # for x in args:
    #     s+=x
    # return s
    # s = x+y+z
    # res = fun(*t)
    print(sum(args))

fun(*t)