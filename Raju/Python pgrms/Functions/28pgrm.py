import copy
def modify(p):
    p[2][1]=100
def main():
    l = [1,2,[7,9,8],3,4,5]
    dup = l.copy()
    modify(dup)
    print(l)
    print(dup)
main()

##########################################################################################

from copy import deepcopy
def modify(p):
    p[2][1]=1234
def main():
    l=[1,2,[3,4,5,6],7,8,9,45]
    dup=deepcopy(l)
    modify(dup)
    print(dup)
    print(l)
main()