import io
f = open("azx.txt","w+")
f.write("hllo for every one")
f.seek(io.SEEK_CUR)
s = f.read()
print(s)
f.close()