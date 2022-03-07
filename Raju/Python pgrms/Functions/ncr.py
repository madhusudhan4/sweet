def fact(a):
    f = 1
    for x in range(1,a+1):
        f = f*x
    return(f)
def nCr(n,r):
    result = fact(n)/(fact(n-r)*fact(r))

    return result
print(nCr(5,2))



