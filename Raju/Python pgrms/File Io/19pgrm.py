
f = open("D:\\Python pgrms\\file\\data.txt")
h = f.read()
f.close()

n=h.split()
d = {}
for l in n:
    if l not in d:
        d[l]=1
    else:
        d[l] +=1
j = max(d.items(),key = lambda x:x[1])
print(j)
