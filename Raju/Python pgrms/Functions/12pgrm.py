def medean(*args):
    l = len(args)
    m = len(args)//2
    sorted_args = sorted(args)
    if l % 2 ==0:
        return (sorted_args[m]+sorted_args[m+1]/2)
    else:
        return (sorted_args[m])

res = medean(45,8,2,1,6,7,4)
print(res)