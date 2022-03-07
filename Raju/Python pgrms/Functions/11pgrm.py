def medean(*args):
    return sorted(args)[len(args)//2]
res = medean(1,2,3,4,9)
print(res)
