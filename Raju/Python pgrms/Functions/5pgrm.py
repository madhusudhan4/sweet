def fact(n):
    f=1
    for x in range(1,1+n):
        f*=x
    return f

result = fact(5)

print(result)
