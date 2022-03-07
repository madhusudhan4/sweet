
def fun():
    pi = 22 / 7

    def area(r):

        print("area:",r*r*pi)

    return area


x=fun()
x(5)
