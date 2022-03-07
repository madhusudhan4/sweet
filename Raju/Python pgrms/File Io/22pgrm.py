def countvc():
    c=v=0
    f=open("ab.txt","r")
    n = f.read()
    for l in n:
        if l.lower() in "aeiou":
            v +=1
        else:
            c+=1
    print(v)
    print(c)
countvc()