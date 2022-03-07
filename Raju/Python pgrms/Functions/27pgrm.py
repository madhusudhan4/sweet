import copy
def modify(p):
    p[1]=454
def main():
    l = [1,2,3,4]
    dup=l.copy()
    modify(dup)
    print(dup)
    print(l)
# if "__name__" == "__main__":
main()

