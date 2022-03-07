import io
f = open("zxy.txt","rb")
f.seek(5,io.SEEK_SET)
print(f.readline())

print(f.tell())

