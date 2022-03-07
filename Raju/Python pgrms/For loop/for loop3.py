for n in range(1,100):
    rt = int(n//2)
    for i in range(2,rt+1):
        if n%i == 0:
            break
    else:
        print(n)
