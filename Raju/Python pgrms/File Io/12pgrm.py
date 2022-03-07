import io
f = open("afg.txt", "a+")
l = "hie"
f.seek(5,io.SEEK_SET)
s = f.readline()
print(s)
f.close()